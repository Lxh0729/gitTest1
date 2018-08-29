#用于评估网站用什么技术
import builtwith
import  whois


#安装指令  pip install python-whois
print(builtwith.parse("http://www.sina.com.cn"))
#网站所有人
print( whois.whois("http://www.sina.com.cn") )