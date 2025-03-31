import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_status(url: str, session: ClientSession, sem: Semaphore):
    print(f"等待获取信号量")
    async with sem:
        print("信号量已获取, 正在发送请求")
        response = await session.get(url)
        print("请求已完成")
        return response.status


async def main():
    sem = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_status("http://www.baidu.com", session, sem) for _ in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())
