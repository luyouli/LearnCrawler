# coding:utf8
import requests
from bs4 import BeautifulSoup
import lxml


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

main_url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
# 由于网站的 Content-Type: text/html 没有指定编码为utf-8，所以默认以unicode 字符集来传输数据，导致乱码，需要用content先下载下来，然后再用str转换即可获得正确的编码
page = requests.get(url=main_url,headers=headers).content
page_text = str(page,'utf-8')
fp = open('sanguo.txt','w',encoding='utf-8')
# 数据解析：章节标题，详情页url，章节内容
soup = BeautifulSoup(page_text,'lxml')
# 定位到所有符合要求的a标签
a_list = soup.select('.book-mulu > ul > li > a')
for a in a_list:
    title = a.string
    detail_url = 'https://www.shicimingju.com' + a['href']
    # 对详情页发起请求解析出章节内容
    page_content_detail = requests.get(url=detail_url,headers=headers).content
    page_text_detail = str(page_content_detail,'utf-8')
    soup = BeautifulSoup(page_text_detail,'lxml')
    div_tag = soup.find('div', class_="chapter_content")
    content = div_tag.text
    fp.write(title + ':' + content + '\n')
    print(title,'保存成功~~')
fp.close()
