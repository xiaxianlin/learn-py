import json
import requests

my_dict = {
    "name": "骆昊",
    "age": 40,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BMW", "max_speed": 240},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 280},
    ],
}

with open("./res/data.json", "w") as file:
    json.dump(my_dict, file)

with open("./res/data.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data)

apiUrl = "http://v.juhe.cn/toutiao/index"  # 接口请求URL
apiKey = "51a7ff5cf33327557b95103f029315f8"  # 在个人中心->我的数据,接口名称上方查看

# 接口请求入参配置
requestParams = {
    "key": apiKey,
    "type": "",
    "page": "",
    "page_size": "",
    "is_filter": "",
}

# 发起接口网络请求
response = requests.get(apiUrl, params=requestParams)

# 解析响应结果
if response.status_code == 200:
    data_model = response.json()
    # 网络请求成功。可依据业务逻辑和接口文档说明自行处理。
    for news in data_model["result"]["data"]:
        print(news["title"])
        print(news["url"])
        print("-" * 60)
else:
    # 网络异常等因素，解析结果异常。可依据业务逻辑自行处理。
    print("请求异常")
