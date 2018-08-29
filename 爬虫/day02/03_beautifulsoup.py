# pip install beautifulsoup4
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# soup = BeautifulSoup(open("test.html"), "html.parser")
soup = BeautifulSoup(html_doc, 'html.parser')
#soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())

print(soup.title)
### <title>The Dormouse's story</title>
##
##print(soup.title.name)
### u'title'
##
print(soup.title.string)
### u'The Dormouse's story'
##
print(soup.title.parent.name)
### u'head'
##
print("soup.p=" , soup.p)
### <p class="title"><b>The Dormouse's story</b></p>
##

print("herf=  " )

print(soup.p["class"])
print(type(soup.a))

# print(soup.p["href"])
print("soup.p.next_sibling= " ,soup.p.next_sibling)
### u'title'
##

#print(soup.a)
### <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
##
print(soup.find_all('a'))
### [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
###  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
###  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
##
print(soup.find(id="link3"))
### <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

##for link in soup.find_all('a'):
##    #print(link.get('href'))
##    print(link['href'])
##    print(link.get_text())
##http://example.com/elsie
##Elsie
##http://example.com/lacie
##Lacie
##http://example.com/tillie
##Tillie

#将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象,
#可以传入一段字符串或一个文件句柄.
#soupF = BeautifulSoup(open("index.html"))
#soupF = BeautifulSoup("<html>data</html>")
#首先,文档被转换成Unicode,并且HTML的实例都被转换成Unicode编码

#Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,
#每个节点都是Python对象,所有对象可以归纳为4种:
#Tag, NavigableString, BeautifulSoup, Comment.
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>','lxml')
# tag = soup.b
# print("type(tag): ",type(tag))
# print("tag: ", tag)
# #tag中最重要的属性: name和attributes

# # name
# print("tag.name: ", tag.name)
# tag.name = "blockquote"
# print("after change, tag: ", tag)

# # attributes
# #一个tag可能有很多个属性. tag<b class="boldest">;
# #有一个 “class”的属性,值为 “boldest”.
# #tag的属性的操作方法与字典相同:
# print('tag["class"]: ', tag["class"])

# # 也可以直接”点”取属性, 比如: .attrs :
# #tag的属性可以被添加,删除或修改.
# #!!!tag的属性操作方法与字典一样!!!
# print("tag.attrs: ",tag.attrs)

# css_soup = BeautifulSoup('<p class="body strikeout"></p>','lxml')
# print(css_soup.p['class'])

# rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>','lxml')
# print(rel_soup.a['rel'])
# # ['index']
# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)
# # <p>Back to the <a rel="index contents">homepage</a></p>

