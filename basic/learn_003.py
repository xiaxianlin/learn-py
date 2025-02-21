import math
# f = float(input("请输入华氏温度: "))
# c = (f - 32) / 1.8
# print("%.1f华氏度 = %.1f摄氏度" % (f, c))
# print(f"{f:.1f}华氏度 = {c:.1f}摄氏度")

radius = float(input("请输入圆的半径: "))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print("周长: %.2f" % perimeter)
print("面积: %.2f" % area)
