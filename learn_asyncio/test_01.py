import asyncio
import aiohttp
from utils import async_timed, fetch_status


@async_timed
async def main():
    connector = aiohttp.TCPConnector(limit=200)
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        url = "http://hadoop.apache.org"
        status = await fetch_status(session, url)
        print(f"status is {status}")


asyncio.run(main())
"""
协程 main 开始执行
status is 200
协程 main 用 0.23856710000000003 秒执行完毕
"""
