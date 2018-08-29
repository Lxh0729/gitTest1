from lxml import etree


html = etree.parse("bookStore.xml")
result = html.xpath("/bookstore/book[price>30.00]/price")
print(len(result))
print(type(result)) #list
print(result[0].text)
print(dir(result[0]))

#
# # print(dir(result[0])) #39.95
#
# #
# result = html.xpath("/bookstore")
# print(result)
# print(len(result))
#
# #result2 = result[0].xpath("book/price")
# result2 = html.xpath("/bookstore/book/price")
# print(result2)
# print(result2[0].text)
# print(result2[1].text)


