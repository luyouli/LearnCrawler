# import scrapy
# 默认管道无法帮我们请求图片数据，因此该管道我们就不用了
class ImgproPipeline:
    def process_item(self, item, spider):
        # scrapy.Request()
        return item

# 管道接收item中的图片地址和名称，在管道中请求到图片的数据，并对其进行持久化存储
from scrapy.pipelines.images import ImagesPipeline # 提供了数据下载功能
import scrapy
class ImgsPipeLine(ImagesPipeline):
    # 根据图片地址发起请求
    def get_media_requests(self, item, info):
        print(item)
        yield scrapy.Request(url=item['src'], meta={'item': item})

    # 返回图片名称
    # def file_path(self, request, response=None, info=None, *, item=None):
    def file_path(self, request, response=None, info=None):
        # 通过request获取meta
        item = request.meta['item']
        filePath = item['name']
        print(item)
        return filePath  # 只返回图片名称

    # 将item传递给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item
