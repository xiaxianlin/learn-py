def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(0, add, 1, 2, 3, 4, 5))
print(calc(1, mul, 1, 2, 3, 4, 5))


def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num**2


old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

old_strings = ["in", "apple", "zoo", "waxberry", "pear"]
new_strings = sorted(old_strings, key=len)
print(new_strings)


import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x**0.5) + 1)))

# 调用Lambda函数
print(fac(6))  # 720
print(is_prime(37))  # True

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int("1001"))  # 1001

print(int2("1001"))  # 9
print(int8("1001"))  # 513
print(int16("1001"))  # 4097

import time
import random
from functools import wraps


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f"{func.__name__}执行时间: {end - start:.2f}秒")
        # 返回被装饰函数的返回值
        return result

    return wrapper


@record_time
def download(filename):
    print(f"开始下载{filename}.")
    time.sleep(random.random() * 6)
    print(f"{filename}下载完成.")


@record_time
def upload(filename):
    print(f"开始上传{filename}.")
    time.sleep(random.random() * 8)
    print(f"{filename}上传完成.")


download("MySQL从删库到跑路.avi")
upload("Python从入门到住院.pdf")
download.__wrapped__("MySQL必知必会.pdf")
upload.__wrapped__("Python从新手到大师.pdf")
