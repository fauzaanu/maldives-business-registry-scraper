import csv
import os
from urllib.parse import urlencode
from crawlee import Request

from apify import Actor
from crawlee.crawlers import HttpCrawler
from crawlee.http_clients import HttpxHttpClient
from crawlee.storages import Dataset
from dotenv import load_dotenv

from .routes import router


async def main(queries: str, max_requests: int = None) -> None:
    """The crawler entry point."""
    if not queries:
        raise Exception("No queries provided")
        crawler = HttpCrawler(
            request_handler=router,
            max_requests_per_crawl=max_requests,
            http_client=HttpxHttpClient(),
        )

        crawlee_requests = []
        for query in queries.split(","):
            # Prepare a POST request to the form endpoint.
            request = Request.from_url(
                url='https://business.egov.mv/BusinessRegistry/SearchBusinessRegistry',
                method='POST',
                headers={'content-type': 'application/x-www-form-urlencoded'},
                use_extended_unique_key=True,
                payload=urlencode(
                    {
                        'query': f'{query}',
                    }
                ).encode(),
            )
            crawlee_requests.append(request)

        await crawler.run(
            crawlee_requests
        )

        await crawler.export_data_csv(
            dataset_name="Businesses",
            path="businesses.csv",
        )
