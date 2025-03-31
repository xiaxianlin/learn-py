import asyncio
from utils import async_timed


async def delay(seconds):
    await asyncio.sleep(seconds)
    if seconds == 3:
        raise ValueError("出现异常了(seconds is 3)")
    return f"我睡了 {seconds} 秒"


@async_timed
async def main():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in (3, 5, 2, 4, 6, 1)]
    for finished_task in asyncio.as_completed(tasks, timeout=4):
        try:
            print(await finished_task)
        except asyncio.TimeoutError:
            print("超时啦")
        except Exception as e:
            print(e)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
