from concurrent.futures import ProcessPoolExecutor
import time


def count(to: int) -> int:
    start = time.perf_counter()
    counter = 0
    while counter < to:
        counter += 1
    end = time.perf_counter()
    print(f"在 {end - start} 秒内将 counter 增加到 {to}")
    return counter


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        numbers = [1, 3, 5, 22, 100000000]
        for result in executor.map(count, numbers):
            print(result)
