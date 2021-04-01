# coding:utf8
import requests
import time
# 线程池模块
from multiprocessing.dummy import Pool

def get_requests(url):
    page_text = requests.get(url=url).text
    return len(page_text)

# 同步代码
# if __name__ == '__main__':
#     start = time.time()
#     urls = [
#         'http://127.0.0.1:5000/Baby',
#         'http://127.0.0.1:5000/jay',
#         'http://127.0.0.1:5000/tom',
#     ]
#     for url in urls:
#         res = get_requests(url)
#         print(res)
#     print('总耗时:',time.time()-start)

# 异步代码
if __name__ == '__main__':
    start = time.time()
    urls = [
        'http://127.0.0.1:5000/Baby',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom',
    ]
    pool = Pool(3)  # 3表示开启线程的数量
    # 使用get_requests作为回调函数，需要基于异步形式对urls列表中的每一列元素进行操作
    # 保证回调函数必须要有一个参数和返回值
    # pool.map(func,alist) # 回调函数 和 列表
    result_list = pool.map(get_requests,urls)
    print(result_list)
    print('总耗时:', time.time() - start)
