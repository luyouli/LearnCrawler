# coding:utf8
import requests
import asyncio
import time
import aiohttp
from lxml import etree

urls = [
    'http://127.0.0.1:5000/Baby',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom',
]

# async def get_request(url):
#     # request是一个不支持异步的模块，所以用aiohttp
#     page_text = requests.get(url).text
#     return page_text

async def get_request(url):
    # 实例化好了一个请求对象
    async with aiohttp.ClientSession() as sess:
        # 调用get发起请求，返回一个响应对象
        # get/post(url,headers,params/data,proxy="http://ip:posr")
        async with await sess.get(url=url) as response:
            # text()获取了字符串形式的响应数据
            # read(）获取byte类型的响应数据
            page_text = await response.text()
            return page_text
# 解析函数的封装
def parse(t):
    # 获取请求到的页面源码数据
    page_text = t.result()
    tree = etree.HTML(page_text)
    parse_text = tree.xpath('//a[@id="feng"]/text()')[0]
    print(parse_text)

if __name__ == '__main__':
    start = time.time()
    tasks = []
    for url in urls:
        c = get_request(url)
        task = asyncio.ensure_future(c)
        task.add_done_callback(parse)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time()-start)
