from types import CodeType
import requests
import json

url = 'http://192.168.1.10:8888/dev/debug/auto'
dic = {"key": "性解放"}
# with open("c:/Users/24071/Downloads/test.json", 'r', encoding='utf-8') as load_f:
#     data = json.load(load_f)

# # headers中添加上content-type这个参数，指定为json格式
# headers = {'Content-Type': 'application/json'}

# post的时候，将data字典形式的参数用json包转换成json格式。
response = requests.get(url=url, params=dic)

print(response)
print(response.content.decode())
