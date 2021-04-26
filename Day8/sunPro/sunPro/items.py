# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    title = scrapy.Field()
    status = scrapy.Field()
    content = scrapy.Field()

class SunproItemDetail(scrapy.Item):
    content = scrapy.Field()
