# coding:utf8
# 单线程+多任务异步协程：
# 1、特殊的函数
# 如果一个函数的定义被async修饰后，该函数就会变成一个特殊的函数
# 该特殊函数调用后，函数内部的实现语句不会被立即执行
# 该特殊函数被调用后会返回一个协程对象

# 2.协程对象
# 对象：通过特殊函数的调用返回一个协程对象
# 协程 == 特殊函数 == 一组指定的操作
# 协程 == 一组指定的操作

# 3.任务对象
# 任务对象就是一个高级的协程对象（任务对象就是对协程对象的进一步封装）
# 任务 == 协程 == 特殊函数 == 一组指定的操作
# 任务 == 一组指定的操作
# 创建任务对象：asyncio.ensure_future(协程对象)
# 任务对象的高级之处：
# 1)可以给任务对象绑定回调：task.add_done_callback(task_callback)
# 2)回调函数的调用时机：任务被执行结束后，才可以调用回调函数
# 3）回调函数的参数只可以有一个：表示的就是该回调函数的调用者（任务对象）
# 4）使用回调函数的参数调用result（）返回的就是任务对象表示的特殊函数return的结果

# 4.事件循环对象
# 对象
# 作用：可以将多个任务对象注册/装载到事件循环对象中，如果开启了事件循环后，则其内部注册/装载的任务对象表示的指定操作就会被基于异步的被执行
# 创建方式：loop = asyncio.get_event_loop()
# 注册且启动方式：loop.run_until_complete(task)

import asyncio
import requests
import time

async def get_request(url):
    print('正在请求的url：',url)
    time.sleep(2)
    print('请求结束:',url)
    return 'Baby'

# 回调函数的封装
# 参数t: 就是该回调函数的调用者（任务对象）
def task_callback(t):
    print('I am task_callback()，参数t',t)
    # result返回的就是特殊函数的返回值
    print('t.result()返回的是：',t.result())

if __name__ == '__main__':
    # c就是一个协程对象
    c = get_request('www.1.com')
    print(c)
    # 任务对象就是对协程对象的进一步封装
    task = asyncio.ensure_future(c)
    # 给task绑定一个回调函数
    task.add_done_callback(task_callback)
    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将任务对象注册到事件循环中且开启事件循环
    loop.run_until_complete(task)
