# coding:utf8
import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
 }

# 使用session捕获并存储cookie
session = requests.Session()
main_url = 'https://xueqiu.com/'
session.get(main_url,headers=headers)  # 捕获并存储cookie
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=187105&size=15'
page_text = session.get(url=url,headers=headers).json()  # 携带cookie发起请求
print(page_text)
