height = float(input("身高(cm)："))
weight = float(input("体重(kg)："))
bmi = weight / (height / 100) ** 2
print(f"{bmi = :.1f}")
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！')

