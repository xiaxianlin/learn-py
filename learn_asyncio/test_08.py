import time
from threading import Thread

def count(to: int):
    start = time.perf_counter()
    counter = 0
    while counter < to:
        counter += 1
    end = time.perf_counter()

    print(f"在 {end - start} 秒内将 counter 增加到 {to}")

if __name__ == '__main__':
    start = time.perf_counter()
    # 多线程和多进程相关的 API 是一致的，只需要将 Process 换成 Thread 即可
    task1 = Thread(target=count, args=(100000000,))
    task2 = Thread(target=count, args=(100000000,))
    task1.start()
    task2.start()
    task1.join()
    task2.join()
    end = time.perf_counter()
    print(f"在 {end - start} 秒内完成")
"""
在 8.974233167000001 秒内将 counter 增加到 100000000
在 8.985212875 秒内将 counter 增加到 100000000
在 8.991764792 秒内完成
"""
