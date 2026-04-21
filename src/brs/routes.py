
from crawlee.router import Router
from crawlee import Request
from crawlee.crawlers import HttpCrawlingContext

from .extractors import RichDataExtractor, BusinessRegistryExtractor

router = Router[HttpCrawlingContext]()
extractor = RichDataExtractor()
business_extractor = BusinessRegistryExtractor()


@router.default_handler
async def default_handler(context: HttpCrawlingContext) -> None:
    """Default request handler with rich data extraction."""
    url = str(context.request.url)
    
    if '/SearchBusinessRegistry' in url:
        print(f'Searching registry...')
    elif '/ViewDetails/' in url:
        print(f'Fetching business details...')

    # Get exact match configuration from request user_data
    exact_match_config = context.request.user_data or {}
    
    # Extract and save rich data to dataset
    await extractor.extract_and_save(context, exact_match_config)
    
    # If this is a search results page, enqueue detail pages for deeper crawling
    if '/SearchBusinessRegistry' in url:
        html_content = (await context.http_response.read()).decode('utf-8')
        businesses = business_extractor.extract_business_listings(html_content, url)
        
        detail_urls = [b['detail_url'] for b in businesses if b.get('detail_url')]
        if detail_urls:
            print(f"Found {len(detail_urls)} business(es)")
            # Pass exact match configuration to detail page requests
            await context.add_requests([
                Request.from_url(url, user_data=exact_match_config) for url in detail_urls
            ])
        else:
            print("No businesses found for this query")
