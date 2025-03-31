import hashlib
import os
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio

def random_password(length: int) -> bytes:
    samples = string.ascii_letters
    return "".join(random.choice(samples) for _ in range(length)).encode("utf-8")

passwords = [random_password(10) for _ in range(10000)]

def hash_password(password: bytes):
    salt = os.urandom(16)
    return hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8)

async def main():
    loop = asyncio.get_running_loop()
    tasks = []
    with ThreadPoolExecutor() as pool:
        for password in passwords:
            tasks.append(loop.run_in_executor(pool, hash_password, password))
        results = await asyncio.gather(*tasks)
        print(len(results))

start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print(end - start)

