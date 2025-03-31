from typing import Dict
from functools import reduce


def map_frequency(text: str) -> Dict[str, int]:
    """
    计算每一行文本中，单词的频率
    """
    words = text.split(" ")
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def merge_dict(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    """
    对两行文本统计出的词频进行合并
    """
    keys = first.keys() | second.keys()
    return {key: first.get(key, 0) + second.get(key, 0) for key in keys}


lines = [
    "I know what I know",
    "I know that I know",
    "I don't know that much",
    "They don't know much",
]

mapped_results = [map_frequency(line) for line in lines]
print(reduce(merge_dict, mapped_results))
"""
{'that': 2, 'know': 6, 'what': 1, 'much': 2, 'They': 1, "don't": 2, 'I': 5}
"""
