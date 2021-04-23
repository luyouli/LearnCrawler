import scrapy
from moviePro.items import MovieproItem

# 组件的作用：
# 引擎（Scrapy）
# 用来处理整个系统的数据流处理，触发事务（框架核心）
# 调度器（Scheduler）
# 用来接受引擎发过来的请求，压入队列中，并在引擎再次请求的时候返回，可以想象成一个URL（抓取网页的网址或者链接）的优先队列，由它来决定下一个要抓取的网址是什么，同时去除重复的网址
# 下载器（Downloader）
# 用于下载网页内容，并将网页内容返回给蜘蛛（Scrapy下载器是建立在twisted这个高效的异步模型上）
# 爬虫（Spiders）
# 爬虫是主要干活的，用于从特定的网页中提取自己需要的信息，即所谓的实体（Item）。用户也可以从中提取出链接，让Scrapy继续抓取下一个页面
# 项目管道（Pipeline）
# 负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据

# 请求传参实现的深度爬取：
# - 深度爬取：爬取的数据没有在同一个页面中（首页数据+详情页数据）
# - 在scrapy中如果没有请求传参那么是无法持久化存储数据的
# - 实现方式：
#     - scrapy.Request(url=,callback=,meta=)
#         - meta是一个字典，可以将meta传递给callback
#     - callback取出meta：
#         - response.meta

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.4567kan.com/index.php/vod/show/id/5.html']

    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            detail_url = 'http://www.4567kan.com' + li.xpath('./div/a/@href').extract_first()

            item = MovieproItem()
            item['title'] = title

            # 对详情页url发起请求
            # meta作用：可以将meta字典传递给callback
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})

    # 用于解析详情页的数据
    def parse_detail(self,response):
        # 接收传递过来的meta
        item = response.meta['item']
        desc = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]').extract_first()
        item['desc'] = desc
        yield item
