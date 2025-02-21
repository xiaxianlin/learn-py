languages = [
    "Python",
    "Java",
    "C++",
    "Python",
]

languages.remove("Python")
print(languages)

tmp = languages.pop(1)
print(tmp)
print(languages)

items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num**2 for num in nums1]
print(nums2)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

import random

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)

n = int(input("生成几注号码: "))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_balls = random.sample(red_balls, 6)
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        print(f"\033[031m{ball:0>2d}\033[0m", end=" ")
    # 从蓝色球列表中随机抽出1个蓝色球
    blue_ball = random.choice(blue_balls)
    # 输出选中的蓝色球
    print(f"\033[034m{blue_ball:0>2d}\033[0m")
