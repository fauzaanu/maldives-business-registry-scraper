# Maldives Business Registry Scraper

This Apify actor scrapes business details from the Maldives Business Registry (https://business.egov.mv/BusinessRegistry) based on provided search queries.

## Features

- **Multiple Business Search**: Search for multiple businesses simultaneously
- **Comprehensive Data Extraction**: Extracts detailed business information including:
  - Basic business information (name, type, status, address)
  - Registration details (number, UPN, SME classification)
  - Management information (owners, directors, shareholders)
  - Business names and activities
  - Permits and licenses information
- **Structured Output**: All data is saved to Apify dataset in structured JSON format
- **Robust Error Handling**: Continues processing even if individual businesses fail

## Input

The actor accepts the following input parameters:

### Required Parameters

- **queries** (array of strings): List of business names or keywords to search for
  - Example: `["investment", "capital", "mart", "hotel"]`
  - Each query will be searched in the business registry

### Optional Parameters

- **maxRequestsPerCrawl** (integer): Maximum number of requests to process
  - Default: 1000
  - Set to limit the crawl scope

## Output

The actor saves all extracted data to the default dataset. Each item in the dataset represents either:

1. **Search Result**: Basic business information from search results
2. **Business Detail**: Comprehensive business information from detail pages

### Sample Output Structure

```json
{
  "business_id": "220307",
  "business_name": "edrova Pvt Ltd",
  "business_type": "Company",
  "status": "Registered",
  "address": "Boduvelu Avah. Muiythoshige L. Maavah, Maldives",
  "registration_number": "C12522023",
  "upn": "2023PV10023A",
  "sme_classification": "Not an SME",
  "managing_director": "Ahmed Javaad",
  "board_of_directors": [
    {
      "name": "Ahmed Javaad",
      "appointed_date": "21-Aug-2023"
    }
  ],
  "shareholders": [
    {
      "name": "Fauzaan Gasim",
      "join_date": "21-Aug-2023"
    }
  ],
  "business_activities": [
    {
      "number": "BP82052023",
      "activity_description": "854901 Education that is not definable by level",
      "state": "Issued",
      "issued_date": "26-Feb-2024"
    }
  ],
  "detail_url": "https://business.egov.mv/BusinessRegistry/ViewDetails/220307?key=-4291927",
  "extracted_at": "2024-01-15T10:30:00.000Z"
}
```

## Use Cases

- **Business Intelligence**: Research competitors or market opportunities
- **Due Diligence**: Verify business registration and status
- **Market Analysis**: Analyze business types and activities in specific sectors
- **OSINT**: Open source intelligence gathering for business research
- **Name Availability**: Check if business names are already taken

## How It Works

1. **Search Phase**: For each query, the actor submits a search request to the business registry
2. **Results Extraction**: Extracts basic business information from search results
3. **Detail Crawling**: Follows links to individual business detail pages
4. **Comprehensive Extraction**: Extracts detailed information from each business page
5. **Data Storage**: Saves all data to Apify dataset in structured format

## Error Handling

The actor is designed to be robust:
- Continues processing even if individual businesses fail to extract
- Logs detailed error information for debugging
- Saves partial data when possible
- Handles network timeouts and retries automatically

## Performance

- Processes multiple businesses concurrently
- Respects rate limits to avoid overwhelming the target site
- Optimized for both speed and data quality
- Configurable request limits for cost control

## Support

For issues or questions about this actor, please check the actor's source code or contact the maintainer.