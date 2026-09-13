import asyncio
import sys
from csoai_defoneos_mcp.server import main

def run():
    sys.exit(asyncio.run(main()))

if __name__ == '__main__':
    run()
