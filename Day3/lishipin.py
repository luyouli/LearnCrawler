# coding:utf8
# 不是我写的，不是我写的，不是我写的
# 源代码地址：https://www.bilibili.com/read/cv9495923/
import requests
import re
import time
import os
from lxml import etree

dirName='./梨视频'
if not os.path.exists(dirName):
    os.mkdir(dirName)

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
}

Target_url='https://www.pearvideo.com/videoStatus.jsp?contId='

url='https://www.pearvideo.com/category_loading.jsp?reqType=5&categoryId=135&start=%d&mrd=0.8710839169846687&filterIds=1717977,1717968,1717750,1717891,1717929,1717770,1717688,1717340,1717299,1717247,1717223,1717184'

page=0
for num in range(1,11):
    print("正在爬取第{}页".format(num))
    if(num==1):
        new_url='https://www.pearvideo.com/category_135'
        Img_page_text=requests.get(new_url,headers=headers).text
        Img_tree=etree.HTML(Img_page_text)
        Img_src_list=Img_tree.xpath('//*[@id="categoryList"]/li/div/a/@href')
        for Img_src in Img_src_list:
            Img_ID=Img_src.replace('video_','')
            cont='cont-'+Img_ID
            Img_src='https://www.pearvideo.com/'+Img_src
            Video_page_text=requests.get(Img_src,headers=headers).text
            Video_tree=etree.HTML(Video_page_text)
            Video_title=Video_tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]+'.mp4'
            Target_Video_url=Target_url+Img_ID
            Video_headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
                'Referer':Img_src
            }
            Target_page_text=requests.get(Target_Video_url,headers=Video_headers).text
            #print(Target_page_text)
            ex='srcUrl":"(.*?)"'
            Video_url=re.findall(ex,Target_page_text,re.S)[0]
            New_Video_url=Video_url.replace(Video_url.split("-")[0].split("/")[-1],cont)
            print(Video_title,New_Video_url)
            with open(dirName+'/'+Video_title,'wb') as fp:
                fp.write(requests.get(New_Video_url,headers=headers).content)

    else:
        page=page+12
        new_url=format(url%page)
        Img_page_text=requests.get(new_url,headers=headers).text
        #print(Img_page_text)
        Img_tree=etree.HTML(Img_page_text)
        Img_src_list=Img_tree.xpath('/html/body/li/div/a/@href')
        print(Img_src_list)
        for Img_src in Img_src_list:
            Img_ID=Img_src.replace('video_','')
            cont='cont-'+Img_ID
            Img_src='https://www.pearvideo.com/'+Img_src
            Video_page_text=requests.get(Img_src,headers=headers).text
            Video_tree=etree.HTML(Video_page_text)
            Video_title=Video_tree.xpath('//*[@id="detailsbd"]/div[1]/div[2]/div/div[1]/h1/text()')[0]+'.mp4'
            Target_Video_url=Target_url+Img_ID
            Video_headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
                'Referer':Img_src
            }

            Target_page_text=requests.get(Target_Video_url,headers=Video_headers).text
            #print(Target_page_text)
            ex='srcUrl":"(.*?)"'
            Video_url=re.findall(ex,Target_page_text,re.S)[0]
            New_Video_url=Video_url.replace(Video_url.split("-")[0].split("/")[-1],cont)
            print(Video_title,New_Video_url)
            with open(dirName+'/'+Video_title,'wb') as fp:
                fp.write(requests.get(New_Video_url,headers=headers).content)

    if(num!=10):
        print("刷新中!")
        time.sleep(2)
