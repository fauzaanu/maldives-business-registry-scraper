# Maldives Business Registry Scraper

A crawler using crawlee-python to scrape business details from https://business.egov.mv/BusinessRegistry

> This crawler is a WIP, however you can get a lot of structured data even now. Some cleanups and handling of pagination for businessnames, and so on are not yet implemented.

### Output sample

> Only meant to be used as a reference for the keys, the actual data is left empty intentionally for reasons.

```json
{
  "business_id": "",
  "detail_url": "",
  "page_type": "business_detail",
  "extracted_at": null,
  "business_name": "",
  "business_type": "",
  "address": "",
  "registration_number": "",
  "status": "Winding Up",
  "upn": null,
  "sme_classification": "",
  "owner": null,
  "managing_director": "",
  "board_of_directors": [
    {
      "name": "",
      "appointed_date": ""
    }
  ],
  "board_of_directors_count": 0,
  "shareholders": [
    {
      "name": "",
      "join_date": ""
    }
  ],
  "shareholders_count": 0,
  "business_names": [],
  "business_names_count": 0,
  "business_activities": [],
  "business_activities_count": 0,
  "permits": {
    "has_permits": "",
    "message": "",
    "permits_list": []
  },
  "licenses": {
    "has_licenses": "",
    "message": "",
    "licenses_list": []
  },
  "domain": "",
  "page_title": "",
  "html_length": "",
  "full_html": ""
}
```

### Running this locally

1. Install UV
2. `uv sync`
3. `uv run python -m crawler`
4. Inside a .env file define the following, replace the queries with your search queries

```.env
QUERIES="mart,ware,investment,capital"
SEPERATOR=","
```

### Running on 

TBA

