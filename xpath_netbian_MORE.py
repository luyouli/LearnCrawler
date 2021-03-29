# coding:utf8
from lxml import etree
import requests
import os

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

dirName = 'GirlsLib'
if not os.path.exists(dirName):
    os.mkdir(dirName)
# 定义一个通用的url模板
url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
for page_range in range(1,175):
    if page_range == 1:
        new_url = 'https://pic.netbian.com/4kmeinv/'
    else:
        new_url = format(url%page_range)

    # response = requests.get(url=url)   # 查看网页原始编码，获得解析方式
    # print(response.encoding)  # 查看网页原始编码
    page = requests.get(url=new_url,headers=headers)
    page.encoding = 'gbk'
    page_text = page.text
    # 图片名称+图片数据
    tree = etree.HTML(page_text)
    # li_list = tree.xpath('//div[@class="slist"]//li')
    # li标签
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    for li in li_list:
        # print(type(li))  # li的数据类型和tree的数据类型是一样的，所以li也可以调用xpath方法
        # print(type(tree))
        title = li.xpath('./a/img/@alt')[0] + '.jpg' # 进行局部数据解析
        img_src = 'https://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_data = requests.get(url=img_src,headers=headers).content
        imgPath = dirName + '/' + title
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
        print(title,'保存成功~')
