import asyncio
from utils import async_timed


@async_timed
async def main():
    task1 = asyncio.create_task(asyncio.sleep(3))
    task2 = asyncio.create_task(asyncio.sleep(3))
    task3 = asyncio.create_task(asyncio.sleep(3))

    await task1
    await task2
    await task3


@async_timed
async def main9():
    tasks = []
    for second in (3, 3, 3):
        task = asyncio.create_task(asyncio.sleep(second))
        tasks.append(task)

    for task in tasks:
        await task


asyncio.run(main9())
