import random

items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ["Python", "Java", "Go", "Kotlin"]
items3 = [100, 12.3, "Python", True]
items4 = list(range(1, 10))
print(items4)
items5 = list("hello")
print(items5)
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ["Python", "Java", "JavaScript"]
print(items5 + items6)
print(items6 + items7)
items5 += items6
print(items5)
print(items6 * 3)
print(items7 * 2)
print(29 in items6)
print(99 in items6)
print("C++" not in items7)
print("Python" not in items7)

items8 = ["apple", "waxberry", "pitaya", "peach", "watermelon"]
print(items8[0])
print(items8[2])
print(items8[4])
items8[2] = "durian"
print(items8)
print(items8[-5])
print(items8[-4])
print(items8[-1])
items8[-4] = "strawberry"
print(items8)
print(items8[1:3:1])
print(items8[0:3:1])
print(items8[0:5:2])
print(items8[-4:-2:1])
print(items8[-2:-6:-1])

print(items8[1:3])
print(items8[:3:1])
print(items8[::2])
print(items8[-4:-2])
print(items8[-2::-1])

items8[1:3] = ["x", "o"]
print(items8)

nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)
print(nums1 != nums2)
print(nums1 <= nums3)
print(nums2 >= nums3)

languages = ["Python", "Java", "C++", "Kotlin"]
for index in range(len(languages)):
    print(languages[index])

for language in languages:
    print(language)

counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f"{face}点出现了{counters[face - 1]}次")
