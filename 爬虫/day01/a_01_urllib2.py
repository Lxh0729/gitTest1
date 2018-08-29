import urllib.request

page= urllib.request.urlopen("http://www.baidu.com")
html=page.read()
print(html)

