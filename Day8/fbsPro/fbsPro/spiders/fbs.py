import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem
# 1. 倒入包 from scrapy_redis.spiders import RedisCrawlSpider
# 2. 修改爬虫父类为：RedisCrawlSpider
# 3. 将start_url替换为redis_keys的属性，属性值为任意字符串
# - redis_key = 'xxx'  表示可以被共享的调度器队列的名称，最终需要将起始的url手动放置到redis_key表示的队列中
# 4. 将数据补充完整


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'sunQueue'   # 可以被共享的调度器队列的名称
    # 稍后我们是需要将一个起始的url手动添加到redis_key表示的队列中

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取全站标题
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title = li.xpath('./span[3]/a/text()').extract_first()
            item = FbsproItem()
            item['title'] = title
            yield item
