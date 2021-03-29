# coding:utf8
# 化妆品生产许可信息管理系统服务平台
# http://scxk.nmpa.gov.cn:81/xk/

import requests
import json

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

# 获取所有企业的ID
# url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=ed59438f34ae47e794f4c7ee5137c1f7'
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
company_id_list = []     # 企业的ID
company_data_list = []   # 企业的详情数据
for page in range(1,6):
    data = {
        'on': 'true',
        'page': str(page),
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
    }

    response = requests.post(url=url,headers=headers,data=data)
    dic_json = response.json()
    # print(dic_json)
    # 'list': [{'ID': 'ed59438f34ae47e794f4c7ee5137c1f7', 'EPS_NAME': '海南京润珍珠生物技术股份有限公司', 'PRODUCT_SN': '琼妆20160001', 'CITY_CODE': '311', 'XK_COMPLETE_DATE': {'date': 25, 'day': 0, 'hours': 0, 'minutes': 0, 'month': 3, 'nanos': 0, 'seconds': 0, 'time': 1619280000000, 'timezoneOffset': -480, 'year': 121}, 'XK_DATE': '2026-04-25', 'QF_MANAGER_NAME': '海南省药品监督管理局', 'BUSINESS_LICENSE_NUMBER': '91460000294121210Y', 'XC_DATE': '2021-04-25', 'NUM_': 1},
    for dic in dic_json['list']:            # 循环获取list列表里面的数据
        company_id_list.append(dic['ID'])   # 将列表里面字典为ID的值写入company_id_list
    # page_test = response.text
    # print(page_test)

# 根据ID获取所有企业的详情数据
# http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=a5ff467ab1b648d590b30aa3cc8a2d56
company_detail_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for company_id in company_id_list:    # 循环获取ID值
    data = {'id': company_id}         # 将ID值赋值给id
    company_detail = requests.post(url=company_detail_url, headers=headers,data=data)
    company_detail_json = company_detail.json()      # 将每次获取到的企业详情数据json化
    company_data_list.append(company_detail_json)    # 将企业详情数据写入到企业的详情数据列表中

with open('./NMPA.json','w',encoding='utf-8') as fp:
    json.dump(company_data_list,fp=fp,ensure_ascii=False)
# fp = open('./NMPA.json','w',encoding='utf-8')
# json.dump(company_data_list,fp=fp,ensure_ascii=False)
