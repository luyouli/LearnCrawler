# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from redis import Redis

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

# 将数据存储到mysql中
class MysqlPipeline(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3308,user='root',password='spider123456',db='spider',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        sql = 'insert into duanziwang values ("%s","%s")'%(item['title'],item['content'])
        # 执行sql，提交事务处理
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item   # 加上这一句，才可以保证优先级低的redis照样可以拿到数据
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

# 将数据存储到redis中，redis模块必须是2.10.x
class RedisPipeline(object):
    conn = None
    def open_spider(self,spider):
        self.conn = Redis(host='127.0.0.1',port=6666,password='666666')
    def process_item(self,item,spider):
        self.conn.lpush('duanziDataRedis',item)
