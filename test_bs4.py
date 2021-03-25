# coding:utf8
from bs4 import BeautifulSoup
import lxml

fp = open('test_bs4.html','r',encoding='utf-8')
soup = BeautifulSoup(fp,'lxml')
print(soup.p)
print(soup.find('div',class_='song'))  # 标签定位
print(soup.find('a',id='feng'))       # 返回的是字符串
print(soup.findAll('a',id='feng'))    # 返回的是列表
print(soup.select('.tang > ul > li'))  # .表示class，#表示id，' '里面放的是选择器，类选择器、id选择器和层级选择器， 大于号表示一个层级，空格表示多个层级
a_tag = soup.find('a',id='feng')
print(a_tag.text)                 # 返回该标签下所有的文本内容 取数据
print(a_tag.string)               # 返回该标签直系的文本内容  取数据
print(a_tag['href'])              # 取属性
