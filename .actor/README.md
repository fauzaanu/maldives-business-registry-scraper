# Maldives Business Registry Scraper

This Apify actor scrapes business details from the [Maldives Business Registry](https://business.egov.mv/BusinessRegistry) based on provided search queries. 

You can also choose to get exact matches only by turning that option on.

## Output

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