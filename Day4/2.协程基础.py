# coding:utf8
# 单线程+多任务异步协程：
# 1、特殊的函数
# 如果一个函数的定义被async修饰后，该函数就会变成一个特殊的函数
# 该特殊函数调用后，函数内部的实现语句不会被立即执行
# 该特殊函数被调用后会返回一个协程对象

import asyncio
import requests
import time

async def get_request(url):
    print('正在请求的url：',url)
    time.sleep(2)
    print('请求结束:',url)

if __name__ == '__main__':
    # c就是一个协程对象
    c = get_request('www.1.com')
    print(c)

    # 任务对象就是对协程对象的进一步封装
    task = asyncio.ensure_future(c)

    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    
    # 将任务对象注册到事件循环中且开启事件循环
    loop.run_until_complete(task)
