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


# 持久化存储
# 基于终端指令的持久化存储
# 要求：该方法只可以将parse方法的返回值存储到本地指定后缀的文本文件中
# 指令：scrapy.exe crawl duanzi -o duanzi.csv

# 基于管道的持久化存储（重点）
# 1.在爬虫文件（duanzi.py）中进行数据解析
# 2.在item.py中定义相关属性，步骤1中解析出来几个字段的数据，就定义几个属性
# 3.在爬虫文件中将解析到的数据存储封装到Item类型的对象中
# 4.将Item类型的对象提交给管道
# 5.在管道文件（pipelines.py）中，接收爬虫文件提交过来的Item类型对象，且对其进行任意形式的持久化操作
# 6.在配置文件（settings.py）中开启管到机制

# 基于管道实现的数据备份
# 将爬取到的数据分别存储到不同的载体
# 实现：将数据一份存储到mysql，一份存储到redis
# 问题：管道文件中一个管道类表示怎么的一组操作呢？
# - 一个管道类对应一种形式的持久化操作，如果将数据存储到不同的载体中就需要使用多个管道类
# 已经定义好三个管道类，将数据写入到三个载体中进行存储：
# - item不会依次把数据提交给三个管道类，只会提交给优先级最高的管道类
# - 优先级高的管道类需要在process_item中实现retun item，才会把item传递给下一个即将被执行的管道类


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
