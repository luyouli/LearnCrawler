# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DuanziproPipeline:
    # 重写父类的两个方法
    def open_spider(self,spider):
        print('我是open_spider()，只会在爬虫开始的时候执行一次')
        self.fp = open('duanzi.txt','w',encoding='utf-8')
    def close_spider(self,spider):
        print('我是close_spider()，只会在爬虫结束的时候执行一次')
        self.fp.close()

    # 该方法是用来接收item对象，一次只能接收一个item，说明该方法会被调用多次
    # 参数item：就是接收到的item对象，item其实就是一个字典
    def process_item(self, item, spider):
        # print(item)
        # 将item存储到文本文件
        self.fp.write(item['title']+':'+item['content']+'\n')
        return item
