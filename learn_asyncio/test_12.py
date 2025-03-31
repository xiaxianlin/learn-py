import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

lock = threading.Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    response = requests.get(
        url,
        verify="/Users/bytedance/py-local/lib/python3.13/site-packages/certifi/cacert.pem",
    )
    with lock:
        counter += 1
    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f"完成请求 {counter}/{request_count}")
        await asyncio.sleep(0.5)


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 1000
        # 将 reporter() 任务加入事件循环
        report_task = asyncio.create_task(reporter(request_count))
        tasks = [
            loop.run_in_executor(pool, get_status_code, "https://www.baidu.com")
            for _ in range(1000)
        ]
        results = await asyncio.gather(*tasks)
        await report_task
        print(all(map(lambda x: x == 200, results)))


asyncio.run(main())
