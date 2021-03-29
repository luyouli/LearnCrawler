# coding:utf8

import requests

# url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='

# 动态数据加载的捕获
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20',
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
response = requests.get(url=url,params=params,headers=headers)
# page_text = response.text
page_text = response.json()
# print(page_text)
for movie in page_text:
    name = movie['title']
    score = movie['score']
    print(name,score)

# with open('./douban.html','w',encoding='utf-8') as fp:
#     fp.write(page_text)


