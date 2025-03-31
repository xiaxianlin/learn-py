import asyncio


async def delay(seconds):
    await asyncio.sleep(seconds)
    if seconds == 3:
        raise ValueError("我出错了(second is 3)")
    print(f"我睡了 {seconds} 秒")


async def main():
    tasks = [asyncio.create_task(delay(seconds)) for seconds in range(1, 6)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    print(f"已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}")
    # 此时未完成的任务仍然在后台运行，这时候我们可以将它们取消掉
    for t in pending:
        t.cancel()
    # 阻塞 3 秒
    await asyncio.sleep(3)


loop = asyncio.new_event_loop()
loop.run_until_complete(main())
"""
我睡了 1 秒
我睡了 2 秒
已完成的任务数: 3
未完成的任务数: 2
"""
