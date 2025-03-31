import asyncio


async def normal_running():
    await asyncio.sleep(3)
    return "正常运行"


async def raise_error():
    raise ValueError("出错啦")


async def main():
    try:
        await asyncio.gather(normal_running(), raise_error())
    except Exception:
        pass
    for task in asyncio.all_tasks():
        # task 相当于对协程做了一个封装，那么通过 get_coro 方法也可以拿到对应的协程
        print(task.get_coro().__name__, task.cancelled())

    results = await asyncio.gather(
        *[task for task in asyncio.all_tasks() if task.get_coro().__name__ != "main"]
    )
    print(results)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
