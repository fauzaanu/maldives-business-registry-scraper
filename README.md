# Maldives Business Registry Scraper

[![Maldives Business Registry Scraper](https://apify.com/actor-badge?actor=fauzaanu/maldives-business-registry-scraper)](https://apify.com/fauzaanu/maldives-business-registry-scraper)

A crawler to scrape business details from https://business.egov.mv/BusinessRegistry. 

Make sure you have [UV Installed](https://docs.astral.sh/uv/getting-started/installation/), and run `uvx --from git+https://github.com/fauzaanu/maldives-business-registry-scraper.git brs "Business one, Business two, Business three"` and get a detailed csv export file at the very end ("businesses.csv"). 

If you choose to [install](#Installing-CLI) the command is as short as running `brs "<comma_seperated_search_terms>"`

You may also run this as an [actor on the APIFY Platform](https://apify.com/fauzaanu/maldives-business-registry-scraper)

## Use cases

- You can pass this to an AI Agent and let it determine which businesses to search for depending on a workflow you create or a list of business names. 
- You can also use this to search whether your new business names were taken or has similiar ones.
- You can also use this as an OSINT tool


### Output sample

| business_id | detail_url | page_type | extracted_at | business_name | business_type | address | registration_number | status | upn | sme_classification | owner | managing_director | board_of_directors | board_of_directors_count | shareholders | shareholders_count | business_names | business_names_count | business_activities | business_activities_count | permits | licenses |
|-------------|------------|-----------|--------------|---------------|---------------|---------|---------------------|--------|-----|--------------------|-------|-------------------|--------------------|--------------------------|--------------|--------------------|----------------|---------------------|--------------------|--------------------------|---------|----------|
| 220307 | https://business.egov.mv/BusinessRegistry/ViewDetails/220307?key=-4291927 | business_detail |  | edrova Pvt Ltd | Company | Boduvelu Avah. Muiythoshige L. Maavah, Maldives | C12522023 | Registered | 2023PV10023A | Not an SME |  | Ahmed Javaad | [{'name': 'Ahmed Javaad', 'appointed_date': '21-Aug-2023'}, {'name': 'Fauzaan Gasim', 'appointed_date': '21-Aug-2023'}] | 2 | [{'name': 'Fauzaan Gasim', 'join_date': '21-Aug-2023'}, {'name': 'Ahmed Javaad', 'join_date': '21-Aug-2023'}] | 2 | [{'name': 'lessonfuse', 'number': 'BN47822023', 'upn': 'BN20231027120C'}, {'name': 'EDZET', 'number': 'BN23202024', 'upn': 'BN20240530640H'}] | 2 | [{'number': 'BP82052023', 'activity_description': '854901 Education that is not definable by level', 'state': 'Issued', 'issued_date': '26-Feb-2024', 'expiry_date': '', 'business_name': '', 'address': 'Boduvelu Avah. Muiythoshige, L. Maavah, Maldives, L. Maavah, Rahdhebai Magu 15071, L. Maavah, Maldives'}, {'number': 'BP37042024', 'activity_description': '854901 Education that is not definable by level', 'state': 'Issued', 'issued_date': '17-May-2024', 'expiry_date': '', 'business_name': '', 'address': 'Muiythoshige, L.Maavah,Maldives, Rahdhebai Magu 15071, L. Maavah, Maldives'}] | 2 | {'has_permits': False, 'message': 'Does not have any business permit owned by edrova Pvt Ltd', 'permits_list': []} | {'has_licenses': False, 'message': 'Does not have any business license owned by edrova Pvt Ltd', 'licenses_list': []} |

### Installing CLI (Local Development)

1. Install UV
2. `uv tool install git+https://github.com/fauzaanu/maldives-business-registry-scraper.git`
3. From now on you can run this with `brs <comma_seperated_search_terms>`

### Running with UVX (One-time Use)

1. Install UV
2. `uvx --from git+https://github.com/fauzaanu/maldives-business-registry-scraper.git brs "<comma_seperated_search_terms>"`
3. (Replace Investment with any <comma_seperated_search_terms>)