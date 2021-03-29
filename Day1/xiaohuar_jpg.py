# coding:utf8

import requests
import urllib
import re
import os

# <div class="col-md-6 col-lg-3">
# 	<div class="card diy-box shadow mb-5">
# 		<a href="/daxue/1381.html" target="_blank"> <img src="http://xiaohuar.com/d/file/p/jump25zowd0.jpg" alt="林沁园大学毕业照" class="card-img-top"> </a>
# 		    <div class="p-2 d-inline-block text-truncate diy-box-title">
# 		<a href="/daxue/1381.html" target="_blank" title="林沁园大学毕业照">林沁园大学毕业照</a>
# 	</div>
# <div class="card-footer text-muted p-2 m-0"> <span> <i class="fa fa-calendar" aria-hidden="true"></i> &nbsp;2020-09-20 </span> <span class="float-right"> <i class="fa fa-fire" aria-hidden="true"></i> &nbsp; </span> </div>
# </div>
# </div>

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

dirName = 'xiaohua'
if not os.path.exists(dirName):
    os.mkdir(dirName)

url = 'http://www.xiaohuar.com/daxue/'
page_text = requests.get(url=url,headers=headers).text

ex = '<div class="col-md-6 col-lg-3">.*?<img src="(.*?)" alt=.*?</div>'
img_src_list = re.findall(ex,page_text,re.S)   # re.S 是处理代码中的“回车”，不处理的话则不会获得图片地址
print(img_src_list)

for src in img_src_list:
    img_path = dirName+'/'+src.split('/')[-1]
    urllib.request.urlretrieve(src,img_path)
    print(img_path,'downloading OK!')

# 或者
# 下面为应对UA的方法

# for src in img_src_list:
#     response = requests.get(url=src,headers=headers).content
#     img_path = dirName + '/' + src.split('/')[-1]
#     with open(img_path,'wb') as fp:
#         fp.write(response)
#         print(img_path,'downloading OK!')
