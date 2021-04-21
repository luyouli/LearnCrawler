import scrapy

from duanziPro.items import DuanziproItem

class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://duanziwang.com/category/经典段子/']

    # 数据解析
    # def parse(self, response):
    #     # 数据解析 名称和内容
    #     article_list = response.xpath('/html/body/section/div/div/main/article')
    #     for article in article_list:
    #         # 下面解析出来的内容不是字符串数据，说明和etree中的xpath使用方式不同
    #         # xpath返回的列表中存储而是Selector对象，其实我们想要的字符串数据被存储到了data属性里面
    #         # 将Selector对象data属性值取出（几乎不用）
    #         # title = article.xpath('./div[1]/h1/a/text()')[0].extract()
    #         # content = article.xpath('./div[2]/p/text()')[0].extract()
    #
    #         # extract_first():将列表中的第一个列表元素表示的Selector对象中的data值取出
    #         title = article.xpath('./div[1]/h1/a/text()').extract_first()
    #         content = article.xpath('./div[2]/p/text()').extract_first()
    #
    #         # 直接使用列表调用extract()：可以将列表中的每一个列表元素表示的Selector中的data值取出
    #         # title = article.xpath('./div[1]/h1/a/text()').extract()
    #         # content = article.xpath('./div[2]/p/text()').extract()
    #
    #         print(title,content)

    # 将解析到的数据进行持久化存储: 基础终端指令的持久化存储
    # def parse(self, response):
    #     all_data = []
    #     # 数据解析 名称和内容
    #     article_list = response.xpath('/html/body/section/div/div/main/article')
    #     for article in article_list:
    #         title = article.xpath('./div[1]/h1/a/text()').extract_first()
    #         content = article.xpath('./div[2]/p/text()').extract_first()
    #         dic = {
    #             'title':title,
    #             'content':content,
    #         }
    #         all_data.append(dic)
    #     return all_data

    # 将解析到的数据进行持久化存储: 基础管道的持久化存储
    def parse(self, response):
        all_data = []
        # 数据解析 名称和内容
        article_list = response.xpath('/html/body/section/div/div/main/article')
        for article in article_list:
            title = article.xpath('./div[1]/h1/a/text()').extract_first()
            content = article.xpath('./div[2]/p/text()').extract_first()

            # 实例化一个item类型的对象，将解析到的数据存储到该对象中
            item = DuanziproItem()
            # 不可以通过.的形式调用属性，只能通过[]调用
            item['title'] = title
            item['content'] = content
            # 将item对象提交给管道
            yield item
