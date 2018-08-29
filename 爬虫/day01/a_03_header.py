import urllib.request
# 添加user-agent
headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
url = "http://www.sina.com.cn"
req = urllib.request.Request(url,headers=headers)
reponse = urllib.request.urlopen(req)
print(reponse.read().decode('utf-8'))



