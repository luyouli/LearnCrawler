# coding:utf8

# 谷歌驱动下载地址
# http://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver
from time import sleep
from lxml import etree
from selenium.webdriver import ActionChains

# 基于浏览器驱动程序实例化一个浏览器对象
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# 对目的网站发起请求
bro.get('https://www.jd.com')
# 标签定位
search_text = bro.find_element_by_xpath('//*[@id="key"]')
search_text.send_keys('花王尿不湿')   # 向标签中录入数据
btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click()    # 点击“搜索”按钮

sleep(5)

# 在搜索结果页面进行滚轮向下滑动（执行js操作：js注入）
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(5)
bro.quit()


url = 'http://scxk.nmpa.gov.cn:81/xk/'
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get(url)
page_text_list = []  #  每一页的页面源码数据
sleep(1)
# 获取当前页面源码数据
page_text = bro.page_source
page_text_list.append(page_text)
sleep(2)

# 点击下一页
for i in range(2):
    next_page = bro.find_element_by_xpath('//*[@id="pageIto_next"]')
    next_page.click()
    sleep(2)
    page_text_list.append(bro.page_source)
for page_text in page_text_list:
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        name = li.xpath('./dl/@title')[0]
        print(name)
sleep(5)
bro.quit()


# 动作链 ActionChains
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get(url)
sleep(2)
# 如果通过find系列的函数进行标签定位，标签是存在于iframe下面，则定位失败
# 解决方法：使用switch_to即可
bro.switch_to.frame('iframeResult')
div_tag = bro.find_element_by_xpath('//*[@id="draggable"]')
# 对div_tag进行滑动操作
action = ActionChains(bro)
action.click_and_hold(div_tag)   # 点击且长按
for i in range(6):
    # div_tag.move_by_offset(10,15)
    action.move_by_offset(10,15).perform()   # perform让动作链立即执行
    sleep(1)
action.release()
bro.quit()


# 规避selenium检测（反爬机制）
# 谷歌无头浏览器
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# 创建浏览器对象
browser = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options)
# 上网
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(5)
browser.save_screenshot('baidu.png')
browser.quit()
