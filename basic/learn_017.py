try:
    with open("./res/致橡树1.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("无法打开指定文件")
except LookupError:
    print("指定了未知的编码")
except UnicodeDecodeError:
    print("读取文件时解码错误")
