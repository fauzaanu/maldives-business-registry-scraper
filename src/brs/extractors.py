import re
from typing import Dict, List, Optional, Any
from urllib.parse import urljoin, urlparse
from parsel import Selector
from crawlee.crawlers import HttpCrawlingContext


class BusinessRegistryExtractor:
    """Extractor for Maldivian Business Registry data."""

    def __init__(self, base_url: str = "https://business.egov.mv"):
        self.base_url = base_url

    def extract_business_listings(self, html_content: str, source_url: str) -> List[Dict[str, Any]]:
        """
        Extract business listings from search results HTML.

        Args:
            html_content: Raw HTML content from the response
            source_url: The URL that was crawled

        Returns:
            List of business data dictionaries
        """
        selector = Selector(text=html_content)
        businesses = []

        # Extract search query from the page
        search_query = self._extract_search_query(selector)

        # Find all business listing containers
        business_cards = selector.css('.feature_home')

        for card in business_cards:
            business_data = self._extract_single_business(card, source_url, search_query)
            if business_data:
                businesses.append(business_data)

        return businesses

    def _extract_search_query(self, selector: Selector) -> Optional[str]:
        """Extract the search query from the page."""
        search_text = selector.css('#search-query::text').get()
        if search_text:
            # Extract query from "Search result for 'Query'"
            match = re.search(r"Search result for ['\"]([^'\"]+)['\"]", search_text)
            return match.group(1) if match else None
        return None

    def _extract_single_business(self, card: Selector, source_url: str, search_query: Optional[str]) -> Optional[
        Dict[str, Any]]:
        """Extract data from a single business card."""
        try:
            # Extract business name
            name_element = card.css('h3 span::text').get()
            if not name_element:
                return None

            business_name = name_element.strip()

            # Extract business type/category from the icon class
            icon_class = card.css('i::attr(class)').get() or ""
            business_category = self._map_icon_to_category(icon_class)

            # Extract business type and status from paragraph texts
            paragraphs = card.css('p::text').getall()
            business_type = None
            status = None

            if len(paragraphs) >= 2:
                business_type = paragraphs[0].strip() if paragraphs[0].strip() else None
                status = paragraphs[1].strip() if paragraphs[1].strip() else None

            # Extract detail link
            detail_link = card.css('a.btn_1::attr(href)').get()
            full_detail_url = urljoin(self.base_url, detail_link) if detail_link else None

            # Extract business ID from the detail link
            business_id = self._extract_business_id(detail_link)

            # Build comprehensive business data
            business_data = {
                'business_name': business_name,
                'business_type': business_type,
                'status': status,
                'business_category': business_category,
                'business_id': business_id,
                'detail_url': full_detail_url,
                'detail_path': detail_link,
                'search_query': search_query,
                'source_url': source_url,
                'icon_class': icon_class,
                'extracted_at': None,  # Will be set when saving to dataset
            }

            # Add metadata
            business_data.update(self._extract_metadata(card, source_url))

            return business_data

        except Exception as e:
            # Log error but don't fail the entire extraction
            print(f"Error extracting business data: {e}")
            return None

    def _map_icon_to_category(self, icon_class: str) -> Optional[str]:
        """Map icon classes to business categories."""
        icon_mapping = {
            'icon_set_1_icon-9': 'Business Name',
            'icon_set_1_icon-29': 'Sole Proprietorship',
            'icon_set_1_icon-43': 'Business Activity',
        }

        for icon, category in icon_mapping.items():
            if icon in icon_class:
                return category

        return 'Unknown'

    def _extract_business_id(self, detail_link: Optional[str]) -> Optional[str]:
        """Extract business ID from detail URL."""
        if not detail_link:
            return None

        # Extract ID from URL like "/BusinessRegistry/ViewDetails/217847?key=-706503270"
        match = re.search(r'/ViewDetails/(\d+)', detail_link)
        return match.group(1) if match else None

    def _extract_metadata(self, card: Selector, source_url: str) -> Dict[str, Any]:
        """Extract additional metadata from the business card."""
        return {
            'has_detail_link': bool(card.css('a.btn_1').get()),
            'card_html': card.get(),  # Store original HTML for debugging
            'domain': urlparse(source_url).netloc,
        }

    def extract_business_details(self, html_content: str, source_url: str) -> Optional[Dict[str, Any]]:
        """
        Extract comprehensive business information from a business detail page.
        """
        add_metadata = False
        # TODO: See the todo in __main__
        try:
            selector = Selector(text=html_content)
            business_id = self._extract_business_id(source_url)

            # Extract main business information from banner
            business_info = self._extract_business_banner(selector)

            # Extract owner/management information (handles both sole proprietorship and companies)
            owner_info = self._extract_owner_info(selector)
            managing_director = self._extract_managing_director(selector)
            board_of_directors = self._extract_board_of_directors(selector)
            shareholders = self._extract_shareholders(selector)

            # Extract business names table
            business_names = self._extract_business_names_table(selector)

            # Extract business activities table
            business_activities = self._extract_business_activities_table(selector)

            # Extract permits and licenses info
            permits_info = self._extract_permits_info(selector)
            licenses_info = self._extract_licenses_info(selector)

            # Build comprehensive detail data
            detail_data = {
                'business_id': business_id,
                'detail_url': source_url,
                'page_type': 'business_detail',
                'extracted_at': None,  # Will be set when saving

                # Main business info
                **business_info,

                # Owner/Management information (varies by business type)
                'owner': owner_info,  # For sole proprietorships
                'managing_director': managing_director,  # For companies
                'board_of_directors': board_of_directors,
                'board_of_directors_count': len(board_of_directors) if board_of_directors else 0,
                'shareholders': shareholders,
                'shareholders_count': len(shareholders) if shareholders else 0,

                # Business names (array of business names owned)
                'business_names': business_names,
                'business_names_count': len(business_names),

                # Business activities (array of activities)
                'business_activities': business_activities,
                'business_activities_count': len(business_activities),

                # Permits and licenses
                'permits': permits_info,
                'licenses': licenses_info,
            }
            if add_metadata:
                detail_data["metadata"] = {
                    # Metadata
                    'domain': urlparse(source_url).netloc,
                    'page_title': selector.css('title::text').get(),
                    'html_length': len(html_content),
                    'full_html': html_content,
                }

            return detail_data

        except Exception as e:
            print(f"Error extracting business details: {e}")
            return {
                'error': str(e),
                'detail_url': source_url,
                'page_type': 'detail_page_error',
                'business_id': self._extract_business_id(source_url),
                'full_html': html_content,  # Always save HTML even on error
                'html_length': len(html_content),
            }

    def _extract_business_banner(self, selector: Selector) -> Dict[str, Any]:
        """Extract main business information from the banner section."""
        banner = selector.css('.businessRegistryBanner')

        # Extract business name and type
        name_element = banner.css('h1.name')
        business_name = name_element.css('::text').get()
        business_type = name_element.css('span::text').get()

        # Clean up the business type (remove brackets)
        if business_type:
            business_type = business_type.strip('[ ]')

        # Extract address
        address = banner.css('p.address::text').get()

        # Extract registration number and status
        number_element = banner.css('p.number')
        number_text = number_element.css('::text').getall()

        registration_number = None
        status = None
        if number_text:
            # First text node is usually the registration number
            registration_number = number_text[0].strip(' ∙').strip()
            # Status is in the span
            status = number_element.css('span::text').get()

        # Extract UPN (Unique Personal Number)
        upn_elements = banner.css('p.number::text').getall()
        upn = None
        for text in upn_elements:
            # UPN patterns: SP for sole proprietorship, PV for companies, etc.
            if len(text.strip()) > 10 and any(prefix in text for prefix in ['SP', 'PV', 'BN']):
                upn = text.strip()
                break

        # Extract SME classification
        sme_classification = banner.css('p.smeClassification::text').get()
        if sme_classification:
            sme_classification = sme_classification.replace('SME Classification: ', '').strip()

        return {
            'business_name': business_name.strip() if business_name else None,
            'business_type': business_type,
            'address': address.strip() if address else None,
            'registration_number': registration_number,
            'status': status.strip() if status else None,
            'upn': upn,
            'sme_classification': sme_classification,
        }

    def _extract_owner_info(self, selector: Selector) -> Optional[str]:
        """Extract owner information (for sole proprietorships)."""
        owner_section = selector.css('div.form_title:contains("Owner")')
        if owner_section:
            owner_name = owner_section.css('p::text').get()
            return owner_name.strip() if owner_name else None
        return None

    def _extract_managing_director(self, selector: Selector) -> Optional[str]:
        """Extract managing director information (for companies)."""
        md_section = selector.css('div.form_title:contains("Managing Director")')
        if md_section:
            md_name = md_section.css('p::text').get()
            return md_name.strip() if md_name else None
        return None

    def _extract_board_of_directors(self, selector: Selector) -> List[Dict[str, Any]]:
        """Extract board of directors from the table."""
        directors = []

        table = selector.css('#homepage-board-directors-list tbody tr')
        for row in table:
            cells = row.css('td::text').getall()
            if len(cells) >= 2:
                directors.append({
                    'name': cells[0].strip(),
                    'appointed_date': cells[1].strip(),
                })

        return directors

    def _extract_shareholders(self, selector: Selector) -> List[Dict[str, Any]]:
        """Extract shareholders from the table."""
        shareholders = []

        table = selector.css('#homepage-shareholders-list tbody tr')
        for row in table:
            cells = row.css('td::text').getall()
            if len(cells) >= 2:
                shareholders.append({
                    'name': cells[0].strip(),
                    'join_date': cells[1].strip(),
                })

        return shareholders

    def _extract_business_names_table(self, selector: Selector) -> List[Dict[str, Any]]:
        """Extract business names from the table."""
        business_names = []

        table = selector.css('#homepage-bn-list tbody tr')
        for row in table:
            cells = row.css('td::text').getall()
            if len(cells) >= 3:
                business_names.append({
                    'name': cells[0].strip(),
                    'number': cells[1].strip(),
                    'upn': cells[2].strip(),
                })

        return business_names

    def _extract_business_activities_table(self, selector: Selector) -> List[Dict[str, Any]]:
        """Extract business activities from the table."""
        activities = []

        table = selector.css('#homepage-business-activity-list tbody tr')
        for row in table:
            cells = row.css('td')
            if len(cells) >= 7:
                # Extract text from each cell
                number = cells[0].css('::text').get()
                activity = cells[1].css('::text').get()
                state = cells[2].css('::text').get()
                issued_date = cells[3].css('::text').get()
                expiry_date = cells[4].css('::text').get()
                business_name = cells[5].css('::text').get()
                address = cells[6].css('::text').get()

                activities.append({
                    'number': number.strip() if number else None,
                    'activity_description': activity.strip() if activity else None,
                    'state': state.strip() if state else None,
                    'issued_date': issued_date.strip() if issued_date else None,
                    'expiry_date': expiry_date.strip() if expiry_date and expiry_date.strip() != '-' else None,
                    'business_name': business_name.strip() if business_name else None,
                    'address': address.strip() if address else None,
                })

        return activities

    def _extract_permits_info(self, selector: Selector) -> Dict[str, Any]:
        """Extract permits information."""
        permits_section = selector.css('div.form_title:contains("Permits")').xpath('following-sibling::div[1]')

        # Check if there's a "Does not have" message
        no_permits_msg = permits_section.css('p::text').get()
        if no_permits_msg and 'Does not have' in no_permits_msg:
            return {
                'has_permits': False,
                'message': no_permits_msg.strip(),
                'permits_list': []
            }

        # If there's a table, extract it (similar to business activities)
        # For now, return basic structure
        return {
            'has_permits': False,
            'message': no_permits_msg.strip() if no_permits_msg else None,
            'permits_list': []
        }

    def _extract_licenses_info(self, selector: Selector) -> Dict[str, Any]:
        """Extract licenses information."""
        licenses_section = selector.css('div.form_title:contains("Licenses")').xpath('following-sibling::div[1]')

        # Check if there's a "Does not have" message
        no_licenses_msg = licenses_section.css('p::text').get()
        if no_licenses_msg and 'Does not have' in no_licenses_msg:
            return {
                'has_licenses': False,
                'message': no_licenses_msg.strip(),
                'licenses_list': []
            }

        # If there's a table, extract it (similar to business activities)
        return {
            'has_licenses': False,
            'message': no_licenses_msg.strip() if no_licenses_msg else None,
            'licenses_list': []
        }


class RichDataExtractor:
    """Enhanced extractor that combines multiple extraction strategies."""

    def __init__(self):
        self.business_extractor = BusinessRegistryExtractor()

    async def extract_and_save(self, context: HttpCrawlingContext) -> None:
        """
        Main extraction method that processes the response and saves rich data.
        """
        try:
            # Get HTML content
            html_content = context.http_response.read().decode('utf-8')
            source_url = str(context.request.url)

            context.log.info(f"Extracting data from {source_url}")

            # Check if this is a search results page or detail page
            if '/SearchBusinessRegistry' in source_url:
                businesses = self.business_extractor.extract_business_listings(html_content, source_url)
                if businesses:
                    context.log.info(f"Extracted {len(businesses)} businesses")
                else:
                    context.log.warning("No businesses extracted from search results")

            elif '/ViewDetails/' in source_url:
                detail_data = self.business_extractor.extract_business_details(html_content, source_url)
                if detail_data:
                    context.log.info(f"Extracted detailed data for: {detail_data.get('business_name', 'Unknown')}")
                    await context.push_data(detail_data, dataset_name="Businesses", )
                else:
                    context.log.warning("No detail data extracted")
            else:
                context.log.warning(f"Unknown page type: {source_url}")

        except Exception as e:
            context.log.error(f"Error during data extraction: {e}")
            import datetime
            await context.push_data({
                'error': str(e),
                'url': str(context.request.url),
                # 'raw_html': html_content[:1000],
                'extracted_at': datetime.datetime.utcnow().isoformat()
            })
