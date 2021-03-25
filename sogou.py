# coding:utf8

import requests

# url = 'https://www.sogou.com/'

keyWord = input('enter a key word:')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
params = {
    'query':keyWord
}
url = 'https://www.sogou.com/web'
response = requests.get(url=url,params=params,headers=headers)
# response.encoding = 'utf-8'
page_text = response.text
fileName = keyWord+'.html'
# with open('./sogou.html','w',encoding='utf-8') as fp:
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName,'is OK !')
