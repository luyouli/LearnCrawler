# coding:utf8
import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
 }

# 获取session
session = requests.Session()

# 验证码识别，基于超级鹰识别
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
# page_text = requests.get(url=url,headers=headers).text   # 这个请求获取cookie，所以把requests换成session以获取session
page_text = session.get(url=url,headers=headers).text

# 解析验证码图片的地址
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]

# 将验证码图片保存到本地
# img_data = requests.get(img_src,headers=headers).content  # 把requests换成session以获取session
img_data = session.get(img_src,headers=headers).content
with open('./code.jpg','wb') as fp:   # 使用wb是因为每次登录都会有新的验证码图片
    fp.write(img_data)

# 识别验证码
code_text = tranformImgCode('./code.jpg',1902)   # tranformImgCode为超级鹰识别，代码没写

login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data = {
    '__VIEWSTATE': 'nZmIEWnq+L5tleyl3VCMrxQ3xaUOSssVkCnIIUSTmC7t5sxGa88uBnJwFS5KsogPmthweUDZR1C2n23PjVMqegdumtPtk8q+BlhID/F+7YCEZglXWYy3cy91uWk='，
    '__VIEWSTATEGENERATOR': 'C93BE1AE'，
    'from': 'http://so.gushiwen.cn/user/collect.aspx'，
    'email': 'kerneler527@163.com'，
    'pwd': 'gushiwenwang2021'，
    'code': code_text， # 将验证码写入‘code’
    'denglu': '登录'，
}

# 对点击登录按钮发起请求，获取了登陆成功后对应的页面源码数据
page_text_login = session.post(url=login_url,headers=headers,data=data).text  # 将requests变为session

# 如果看到一组乱序的请求参数，要去验证这组请求参数是否为动态变化的
# 在这个网站为'__VIEWSTATE'和'__VIEWSTATEGENERATOR'
# 方式1：一般来说动态变化的请求参数会隐藏在前台页面中，我们就要去前台页面源码里面找
# 方式2：如果前台页面没有，那么就基于抓包工具全局搜索
