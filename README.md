# Maldives Business Registry Scraper

A crawler to scrape business details from https://business.egov.mv/BusinessRegistry

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
### Installing CLI
1. Install UV
2. uv tool install git+https://github.com/fauzaanu/maldives-business-registry-scraper.git@cli 
3. From now on you can run this with `brs <comma_seperated_search_terms>`


### Running with UVX (one time runs/passing to an AI agent)

1. Install UV
2. `uvx --from git+https://github.com/fauzaanu/maldives-business-registry-scraper.git@cli brs "Investment"`
3. (Replace Investment with any <comma_seperated_search_terms>)