import scrapy

# 中间件：
# - 作用：批量拦截请求和响应
# - 爬虫中间件
# - 下载中间件（推荐）
#     - 拦截请求：
#         - 篡改请求url
#         - 伪装请求头信息
#             - UA
#             - Cookie
#         - 设置请求代理（重点）
#     - 拦截响应
#         - 篡改响应数据
#     - 代理操作必须使用中间件才可以实现
#         - process_exception:
#             - request.meta['proxy'] = 'http://ip:port'

class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/','https://www.sogou.com']

    def parse(self, response):
        print(response)
