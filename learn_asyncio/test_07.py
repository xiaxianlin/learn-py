import asyncio


async def delay(seconds):
    await asyncio.sleep(seconds)
    if seconds == 3:
        raise ValueError("我出错了(second is 3)")
    return f"我睡了 {seconds} 秒"


async def main():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in range(1, 6)]
    while True:
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for t in done:
            exc = t.exception()
            print(exc) if exc else print(t.result())

        if pending:  # 还有未完成的任务，那么继续使用 wait
            tasks = pending
        else:
            break


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""
我睡了 1 秒
我睡了 2 秒
我出错了(second is 3)
我睡了 4 秒
我睡了 5 秒
"""
