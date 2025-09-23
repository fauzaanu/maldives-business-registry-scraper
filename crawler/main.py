import os
from urllib.parse import urlencode
from crawlee import Request

from apify import Actor
from crawlee.crawlers import HttpCrawler
from crawlee.http_clients import HttpxHttpClient
from dotenv import load_dotenv

from .routes import router


async def main() -> None:
    """The crawler entry point."""
    async with Actor:
        crawler = HttpCrawler(
            request_handler=router,
            max_requests_per_crawl=None,
            http_client=HttpxHttpClient(),
        )
        load_dotenv()
        queries = os.getenv("QUERIES")
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
