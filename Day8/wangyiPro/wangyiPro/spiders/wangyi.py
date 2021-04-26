import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    model_urls = [] # 每一个板块对应的url

    # 实例化一个全局的浏览器对象
    bro = webdriver.Chrome(executable_path='./chromedriver')

    # 数据解析：每一个板块对应的url
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        indexs = [3,4,6,7,8]
        for index in indexs:
            model_li = li_list[index]
            model_url = model_li.xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        # 对每一个板块的url发起请求
        for url in self.model_urls:
            yield scrapy.Request(url=url,callback=self.parse_model)
    # 数据解析：新闻标题+新闻详情页url（动态加载的数据）
    def parse_model(self,response):
        # 直接对response解析新闻标题数据是无法获取数据（因为是动态加载数据）
        # response是不满足当下需求的，需要将其变成符合要求的response（包含动态加载数据的）
        # 两者区别就是：响应数据不同
        # 使用中间件将不满足需求的响应对象中的响应数据篡改成包含动态加载数据的响应数据，将其变成满足需求的响应对象
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            if new_detail_url:  # 如果new_detail_url不为空，则发请求
                item = WangyiproItem()
                item['title'] = title
                # 对新闻详情页url发起请求
                yield scrapy.Request(url=new_detail_url,callback=self.parse_new_detail,meta={'item':item})
    def parse_new_detail(self,response):
        # 解析新闻内容
        content = response.xpath('//*[@id="content"]/div[2]/p/text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content

        yield item
    # 爬虫类父类的方法，该方法是在爬虫结束最后一刻执行
    def closed(self,spider):
        self.bro.quit()
