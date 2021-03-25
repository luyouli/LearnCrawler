# coding:utf8

import requests
import urllib

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

# 方式1
img_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic1.win4000.com%2Fpic%2Fc%2F87%2F8df3265979.jpg&refer=http%3A%2F%2Fpic1.win4000.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1618715447&t=beaa01148ac78b53797897db6c5b6f2a'
response = requests.get(url=img_url,headers=headers)
img_data = response.content  # content 返回二进制形式的响应数据
with open('1.jpg','wb') as fp:
    fp.write(img_data)

# 方式2  无法使用UA伪装
img_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic1.win4000.com%2Fpic%2Fc%2F87%2F8df3265979.jpg&refer=http%3A%2F%2Fpic1.win4000.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1618715447&t=beaa01148ac78b53797897db6c5b6f2a'
urllib.request.urlretrieve(img_url,'2.jpg')
