import urllib.request
from bs4 import BeautifulSoup  # 使用BeautifulSoup解析网页

root_url = "https://www.aliyun.com"
page = urllib.request.urlopen(root_url)

soup = BeautifulSoup(page, 'html.parser')
print(soup.body.text)

links = soup.findAll('a')  # 找到所有a节点
# for link in links:
# print(link['href'])  # 打印他的href属性
