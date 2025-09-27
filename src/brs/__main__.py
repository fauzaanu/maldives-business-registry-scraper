import argparse
import asyncio
import os

from dotenv import load_dotenv

from .main import main


def cli_main():
    """Entry point for the crawler CLI."""
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Run the business registry crawler')
    parser.add_argument(
        'queries', 
        nargs='?', 
        help='Comma-separated search queries (e.g., "company1,company2,company3")'
    )
    
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
    cli_main()
