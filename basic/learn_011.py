a, b, *c = range(1, 5)
print(a, b, c)
a, b = b, a
print(a, b)

import timeit

print("%.3f 秒" % timeit.timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10000000))
print("%.3f 秒" % timeit.timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10000000))

infos = ("骆昊", 43, True, "四川成都")
# 将元组转换成列表
print(list(infos))  # ['骆昊', 43, True, '四川成都']

frts = ["apple", "banana", "orange"]
# 将列表转换成元组
print(tuple(frts))  # ('apple', 'banana', 'orange')
