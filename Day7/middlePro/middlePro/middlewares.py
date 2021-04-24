from scrapy import signals
# 下载中间件是用来批量拦截请求和响应
class MiddleproDownloaderMiddleware:
    # 拦截所有的请求（正常&异常）
    # 参数：request就是拦截到的请求，spider爬虫类实例化对象
    def process_request(self, request, spider):
        print('process_request()')
        request.headers['User-Agent'] = 'xxx'
        # request.headers['Cookie'] = 'xxx'
        return None

    # 拦截所有的响应对象
    # 参数：response拦截到的响应对象，request响应对象对应的请求对象
    def process_response(self, request, response, spider):
        print('process_response()')
        return response

    # 拦截异常的请求
    # 参数：request就是拦截到的发生异常的请求
    # 作用：想要将异常请求进行修正，变成正常的请求，对其进行重新发送
    def process_exception(self, request, exception, spider):
        request.meta['proxy'] = 'http://ip:port' # 设置代理
        print('process_exception()')
        return request # 将异常请求修正后重新发送
        # pass
