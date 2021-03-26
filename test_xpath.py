# coding:utf8
from lxml import etree

# 解析原理：html标签是以树状的形式进行展示
# 1.实例化一个etree对象，且将待解析的页面源码数据加载到该对象中
# 2.调用etree对象的xpath方法结合不同的xpath表达式实现标签的定位和数据的提取

# 实例化etree对象
# etree.parse（‘filename’）：将本地html文件加载到该对象中
# etree.HTML（page_text）：网站获取的页面数据加载到该对象
tree = etree.parse('test_bs4.html')


# 标签定位：
# 最左侧的/：如果xpath表达式最左侧以/开头，表示一定要从根标签开始定位指定标签
# 非最左侧的/：表示一个层级
# 非最左侧的//：表示多个层级
# 最左侧的//：xpath表示可以从任意位置进行标签定位，所有的meta
tree.xpath('/html/head/meta')   # 定位meta
tree.xpath('/html//meta')       # 定位meta
tree.xpath('//meta')            # 定位meta
# 属性定位：//tagName[@attrName="value"]
# 定位class为song的div下面所有的p标签
tree.xpath('//div[@class="song"]/p')
# 索引定位：//tagName[index]:索引从1开始
# 定位class为song的div下面第二个p
tree.xpath('//div[@class="song"]/p[2]')
# 模糊匹配
tree.xpath('//div[contains(@class,"ng")]')
tree.xpath('//div[starts-with(@class,"ta")]')

# 取文本：
tree.xpath('//div[@class="song"]/p[2]/text()')    # 直系文本内容
tree.xpath('//div[@class="song"]/p[2]//text()')   # 所有文本内容
# 取属性：
# /@attrName
tree.xpath('//a[@id="feng"]/@href')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
