# coding:utf8

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

for page in range(1,9):
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': str(page),
        'pageSize': '10',
    }

    # data参数是post方法中处理参数动态化的参数
    response = requests.post(url=url,headers=headers,data=data)
    page_text = response.json()
    # print(page_text)
    for dic in page_text['Table1']:
        title = dic['storeName']
        addr = dic['addressDetail']
        print(title,addr)

