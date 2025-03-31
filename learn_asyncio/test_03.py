import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed
async def main():
    connector = aiohttp.TCPConnector(limit=200)
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        requests = [
            fetch_status(session, "http://hadoop.apache.org") for _ in range(100)
        ]
        status_codes = await asyncio.gather(*requests)
        print(len(status_codes))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
