import requests

# print(help(requests.get))
# 发送请求 get请求
respons = requests.get("http://www.baidu.com")
respons_code = respons.status_code
if respons_code == 200:
    print("获取成功 ," ,"状态码为 ： " ,respons_code)
    print(respons.text)
elif respons_code !=200:
    if  500<respons_code< 600:
        print("请求失败，获取数据不对")
respons.encoding="utf-8"

print(respons.text)


# 官方说明
# >> > import requests
# >> > r = requests.get('https://www.python.org')
# >> > r.status_code
# 200
# >> > 'Python is a programming language' in r.content
# True
#
# ... or POST:
#
# >> > payload = dict(key1='value1', key2='value2')
# >> > r = requests.post('http://httpbin.org/post', data=payload)
# >> > print(r.text)
# {
#     ...
# "form": {
#     "key2": "value2",
#     "key1": "value1"
# },
# ...
# }
