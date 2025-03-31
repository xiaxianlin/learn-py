import time
from typing import Dict, List
from functools import reduce
from concurrent.futures import ProcessPoolExecutor
import asyncio


def partition(data: List, chunk_size: int) -> List:
    """
    将一个大型列表，以 chunk_size 为单位，分割成若干个小列表（chunk）
    """
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    """
    计算一个 chunk 中，单词的频率
    """
    frequencies = {}
    # chunk 的每一行都是如下格式：单词\t年份\t出现次数\t出现在多少本书中
    for line in chunk:
        word, _, count, _ = line.split("\t")
        if word in frequencies:
            frequencies[word] += int(count)
        else:
            frequencies[word] = int(count)

    return frequencies


def merge_dict(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:

    keys = first.keys() | second.keys()
    return {key: first.get(key, 0) + second.get(key, 0) for key in keys}


async def main(chunk_size):
    with open(
        r"./learn_asyncio/googlebooks-eng-all-1gram-20120701-a", encoding="utf-8"
    ) as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.perf_counter()
        with ProcessPoolExecutor() as pool:
            for chunk in partition(contents, chunk_size):
                tasks.append(loop.run_in_executor(pool, map_frequencies, chunk))
            middle_results = await asyncio.gather(*tasks)
            final_results = reduce(merge_dict, middle_results)
            print(f"Aardvark 总共出现了 {final_results['Aardvark']} 次")
            end = time.perf_counter()
            print(f"MapReduce 总耗时: {end - start}")


if __name__ == "__main__":
    asyncio.run(main(1000000))
