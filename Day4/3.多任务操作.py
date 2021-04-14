# coding:utf8

# 重要注意事项
# 在特殊函数内部不可以出现不支持异步模块对应的代码，否则会中断整个异步效果

# 在特殊函数内部，凡是阻塞操作前，都必须使用await进行修饰，await可以保证阻塞操作在异步执行过程中不会被跳过

import asyncio
import requests
import time

async def get_request(url):
    print('正在请求的url：',url)
    # time.sleep(2)  # 在特殊函数内部不可以出现不支持异步模块对应的代码，否则会中断整个异步效果，time不支持异步
    # asyncio.sleep(2)   # 阻塞被跳过了，因为没有await
    await asyncio.sleep(2)
    print('请求结束:',url)
    return 'Baby'

urls = {
    'www.1.com',
    'www.2.com',
    'www.3.com',
}

if __name__ == '__main__':
    start = time.time()
    tasks = []  # 多任务列表
    # 1.创建协程对象
    for url in urls:
        c = get_request(url)
        # 2.创建任务对象
        task = asyncio.ensure_future(c)
        tasks.append(task)
    # 3.创建事件循环对象
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(tasks)
    # 必须使用wait方法对tasks进行封装才行
    loop.run_until_complete(asyncio.wait(tasks))  # wait方法的作用是将任务列表中的任务对象赋予可被挂起的权限
                                                  # 挂起：将当前任务对象交出CPU使用权
    print(time.time()-start)
