#! /usr/bin/env python

"""
Given a LangGraph server API url, this script will show all the deployed graphs on the server.

Usage:
$ python show_deployed_graphs.py <API URL>
"""

from langgraph_sdk import get_client
import asyncio
import sys
from pprint import pprint

# URL from command line
if len(sys.argv) < 2:
    print("Usage: python show_deployed_graphs.py <API URL>")
    sys.exit(1)
URL = sys.argv[1]

client = get_client(url=URL)

async def main():
	# Search all hosted graphs
	assistants = await client.assistants.search()
	pprint(assistants)

asyncio.run(main())