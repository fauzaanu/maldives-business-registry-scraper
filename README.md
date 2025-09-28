# Maldives Business Registry Scraper

[![Maldives Business Registry Scraper](https://apify.com/actor-badge?actor=fauzaanu/maldives-business-registry-scraper)](https://apify.com/fauzaanu/maldives-business-registry-scraper)

A crawler to scrape business details from [Maldives Business Registry](https://business.egov.mv/BusinessRegistry. )

Make sure you have [UV Installed](https://docs.astral.sh/uv/getting-started/installation/), then run `uvx --from git+https://github.com/fauzaanu/maldives-business-registry-scraper.git brs "Business one, Business two, Business three"` and get a detailed csv export file at the very end : `businesses.csv`

If you choose to [install](#Installing-CLI) the command is as short as running `brs "<comma_seperated_search_terms>"`

You may also run this as an [actor on the Apify Platform](https://apify.com/fauzaanu/maldives-business-registry-scraper)

### Output sample

> The actual datafiles will have the following structure, The CLI also does an export of all the datafiles combined in one CSV at the very end for convenience.

```json
{
  "business_id": "314159",
  "detail_url": "https://business.example.com/BusinessRegistry/ViewDetails/314159?key=271828",
  "page_type": "business_detail",
  "extracted_at": "2025-10-02T14:30:45.678901",
  "business_name": "THORNHILL INDUSTRIES Pvt Ltd",
  "business_type": "Company",
  "address": "H. SAMARITAN TOWER, 3rd FLOOR",
  "registration_number": "C04212021",
  "status": "Registered",
  "upn": "2021PV07742D",
  "sme_classification": "Large",
  "owner": null,
  "managing_director": "HAROLD FINCH",
  "board_of_directors": [
    {
      "name": "John Reese",
      "appointed_date": "10-Sep-2021"
    },
    {
      "name": "HAROLD FINCH",
      "appointed_date": "10-Sep-2021"
    }
  ],
  "board_of_directors_count": 2,
  "shareholders": [
    {
      "name": "John Reese",
      "join_date": "10-Sep-2021"
    },
    {
      "name": "Samantha Groves",
      "join_date": "10-Sep-2021"
    },
    {
      "name": "HAROLD FINCH",
      "join_date": "10-Sep-2021"
    }
  ],
  "shareholders_count": 3,
  "business_names": [
    {
      "name": "Northern Lights Solutions",
      "number": "BN98762025",
      "upn": "BN20250409999J"
    }
  ],
  "business_names_count": 4,
  "business_activities": [
    {
      "number": "BP56782023",
      "activity_description": "6201 Computer programming activities",
      "state": "Issued",
      "issued_date": "15-Mar-2030",
      "expiry_date": "",
      "business_name": "",
      "address": "M. Thornhill, Liberty Lane 67890, Metropolis, Example Nation"
    }
  ],
  "business_activities_count": 3,
  "permits": {
    "has_permits": false,
    "message": "Does not have any business permit owned by THORNHILL INDUSTRIES Pvt Ltd",
    "permits_list": []
  },
  "licenses": {
    "has_licenses": false,
    "message": "Does not have any business license owned by THORNHILL INDUSTRIES Pvt Ltd",
    "licenses_list": []
  }
}
```

### Installing CLI (Local Development)

1. Install UV
2. `uv tool install git+https://github.com/fauzaanu/maldives-business-registry-scraper.git`
3. From now on you can run this with `brs <comma_seperated_search_terms>`

### Running with UVX (One-time Use)

1. Install UV
2. `uvx --from git+https://github.com/fauzaanu/maldives-business-registry-scraper.git brs "<comma_seperated_search_terms>"`
3. (Replace Investment with any <comma_seperated_search_terms>)
