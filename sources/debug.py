from types import CodeType
import requests
import json

url = 'http://192.168.1.10:8888/dev/debug'
with open("./sources/m.aaread.club.json", 'r', encoding='utf-8') as load_f:
    data = json.load(load_f)

# headers中添加上content-type这个参数，指定为json格式
headers = {'Content-Type': 'application/json'}

# post的时候，将data字典形式的参数用json包转换成json格式。
response = requests.post(url=url, data=json.dumps(data))

print(response)

print(response.content.decode())
