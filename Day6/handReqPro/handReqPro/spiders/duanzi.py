import scrapy
from handReqPro.items import HandreqproItem

scrapy手动请求发送实现全站数据爬取
- yield scrapy.Request(url=,callback=)
    callback指定解析函数，用于解析数据
- yield scrapy.FormRequest(url=,callback=,formdata=):POST
    fordata：字典，请求参数


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://duanziwang.com/category/经典段子/1/']

    # 通用url模板
    url = 'http://duanziwang.com/category/经典段子/%d/'
    page_num = 2

    # 将段子网中所有页码对应的数据进行爬取
    def parse(self, response):
        # 数据解析 名称和内容
        article_list = response.xpath('/html/body/section/div/div/main/article')
        for article in article_list:
            title = article.xpath('./div[1]/h1/a/text()').extract_first()
            content = article.xpath('./div[2]/p/text()').extract_first()
            item = HandreqproItem()
            item['title'] = title
            item['content'] = content
            yield item
        if self.page_num < 5:
            new_url = format(self.url%self.page_num)   # 其它页码完整url
            self.page_num += 1
            # 对新的页码对应的url进行请求发送(手动请求发送)
            yield scrapy.Request(url=new_url,callback=self.parse)


