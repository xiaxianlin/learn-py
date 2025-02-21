import re

# 创建正则表达式对象，使用了前瞻和回顾来保证手机号前后不应该再出现数字
pattern = re.compile(r"(?<=\D)1[34578]\d{9}(?=\D)")
sentence = """重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765。"""
# 方法一：查找所有匹配并保存到一个列表中
tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)
print("--------华丽的分隔线--------")

# 方法二：通过迭代器取出匹配对象并获得匹配的内容
for temp in pattern.finditer(sentence):
    print(temp.group())
print("--------华丽的分隔线--------")

# 方法三：通过search函数指定搜索位置找出所有匹配
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence, m.end())

sentence = "Oh, shit! 你是傻逼吗? Fuck you."
purified = re.sub(
    "fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]", "*", sentence, flags=re.IGNORECASE
)
print(purified)

poem = "窗前明月光，疑是地上霜。举头望明月，低头思故乡。"
sentences_list = re.split(r"[，。]", poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)
