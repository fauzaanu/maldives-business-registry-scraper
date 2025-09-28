import argparse
import asyncio
import os
import sys

from dotenv import load_dotenv
from apify import Actor


async def main():
    """Main entry point that handles both CLI and Apify modes."""
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Run the business registry crawler')
    parser.add_argument(
        'queries', 
        nargs='?', 
        help='Comma-separated search queries (e.g., "company1,company2,company3")'
    )
    parser.add_argument(
        '--apify', 
        action='store_true',
        help='Run in Apify mode (used internally by Apify platform)'
    )
    
    args = parser.parse_args()
    
    async with Actor:
        if args.apify:
            # Apify mode - get input from Apify platform
            actor_input = await Actor.get_input() or {}
            queries_list = actor_input.get('queries', [])
            max_requests = actor_input.get('maxRequestsPerCrawl')
            
            if not queries_list:
                Actor.log.error('No queries provided in input!')
                await Actor.fail('No queries provided. Please specify business names to search for.')
                return
            
            queries = ','.join(queries_list)
            Actor.log.info(f'Starting scraper with queries: {queries}')
            if max_requests:
                Actor.log.info(f'Max requests per crawl: {max_requests}')
        else:
            # CLI mode - get queries from arguments or environment
            print("Running in CLI Mode . . ")
            queries = args.queries or os.getenv("QUERIES")
            max_requests = None
            
            if not queries:
                print("Error: No queries provided. Use either:")
                print("  uv run python -m crawler 'query1,query2,query3'")
                print("  or set QUERIES environment variable")
                exit(1)
        
        # Import and call the crawler main function
        from .main import main as crawler_main
        await crawler_main(queries, max_requests)
        
        if args.apify:
            Actor.log.info('Scraper completed successfully!')


def cli_main():
    """Sync wrapper for CLI entry point."""
    asyncio.run(main())


if __name__ == '__main__':
    cli_main()
