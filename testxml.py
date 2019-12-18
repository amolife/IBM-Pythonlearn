import requests
import os

heads = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101"
         "Firefox/68.0", }
url = "https://www.baidu.com/"
html = requests.get(url, params={'wd': '123'}, timeout=1, headers=heads)
content = html.content
# print(content.decode('utf-8'))
# print(content)
# print(type(content))
#with open('./testxml.txt', 'wb') as fw:
#    fw.write(content)
#with open('./testxml.txt', 'rb') as fr:
#    print('print 100 bytes:', fr.read(100))
print(u"$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(html.text)
print(html.status_code)
print(html.encoding)
print(html.headers)
print(html.headers['Date'])
print(html.cookies)
print("##############################")


