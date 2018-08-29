import urllib.request
import urllib.error
# from urllib import  error 或者
import  time



#全局
ua = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"

def  download(urlin  ,retry_num, uain=ua):
    try:
        # 添加user-agent
        headers = {"User-Agent":uain}
        req = urllib.request.Request(urlin,headers=headers)
        reponse = urllib.request.urlopen(req)
        # print(reponse.read().decode('utf-8'))
        with open("test.html" , "wb") as f:
            f.write(reponse.read())
    except urllib.error.URLError:
        print("地址错误")
    except urllib.error.HTTPError:
        print("服务器错误")
        print("time  sleep  5s")
        time.sleep(5)
        download(urlin, uain)







if __name__ == '__main__':
    # ua = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
    url = "http://www.baidu.com"
    download(url )






