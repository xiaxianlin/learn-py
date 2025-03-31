import time
from functools import wraps
from typing import Callable, Any
from aiohttp import ClientSession


def async_timed(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        print(f"协程 {func.__name__} 开始执行")
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            total = end - start
            print(f"协程 {func.__name__} 用 {total} 秒执行完毕")

    return wrapper


async def fetch_status(session: ClientSession, url: str):
    async with session.get(url) as response:
        return response.status
