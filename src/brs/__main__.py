import argparse
import asyncio
import os
import sys

from dotenv import load_dotenv
from apify import Actor

from .main import main


async def apify_main():
    """Entry point for Apify actor."""
    async with Actor:
        # Get input from Apify
        actor_input = await Actor.get_input() or {}
        
        # Extract queries from input
        queries_list = actor_input.get('queries', [])
        max_requests = actor_input.get('maxRequestsPerCrawl')
        
        if not queries_list:
            Actor.log.error('No queries provided in input!')
            await Actor.fail('No queries provided. Please specify business names to search for.')
            return
        
        # Convert list to comma-separated string for existing main function
        queries = ','.join(queries_list)
        
        Actor.log.info(f'Starting scraper with queries: {queries}')
        if max_requests:
            Actor.log.info(f'Max requests per crawl: {max_requests}')
        
        # Use existing main function
        await main(queries, max_requests)
        
        Actor.log.info('Scraper completed successfully!')


def cli_main():
    """Entry point for the crawler CLI."""
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Run the business registry crawler')
    parser.add_argument(
        'queries', 
        nargs='?', 
        help='Comma-separated search queries (e.g., "company1,company2,company3")'
    )

    # TODO: ADD ARG to conditionally add metadata
    
    args = parser.parse_args()
    
    # args take priority over ENV
    queries = args.queries or os.getenv("QUERIES")
    
    if not queries:
        print("Error: No queries provided. Use either:")
        print("  uv run python -m crawler 'query1,query2,query3'")
        print("  or set QUERIES environment variable")
        exit(1)
    
    asyncio.run(main(queries))


if __name__ == '__main__':
    # Simple check: if we have command line arguments, use CLI mode
    # Otherwise, assume we're running on Apify platform
    if len(sys.argv) > 1:
        cli_main()
    else:
        asyncio.run(apify_main())
