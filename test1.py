# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:05:39 2018

@author: CHENKM2
"""
import requests
from lxml import etree
import time
import os
    # 向网页请求数据，老套路了
def get_one_page(url):
   try:
       headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
       }
       reponse = requests.get(url,headers = headers)
       if reponse.status_code == 200:
           return reponse.text
       return None
   except  requests.exception:
       return None
def get_one_parse(url):
    
    file = os.getcwd()
    with open(os.path.join(file,'456.txt'), 'a+') as f: # 保存在相应的文件里
       print(url) # 看爬取到第几页来了
       html = get_one_page(url)
       html = etree.HTML(html)# 从获得的html页面中分析提取出所需要的数据
       IP = html.xpath('.//*[@id="list"]/table/tbody//td[1]/text()') # 解析到相应的位置，用我上次教大家的方法，很方便的
       poots = html.xpath('.//*[@id="list"]/table/tbody//td[2]/text()')# 这是 端口位置
       for (ip,poot) in zip(IP,poots): # 保存
           ip = ip +':' +  poot
           print("测试：{}".format(ip))
           f.write(ip + '\n')
           #validate(ip)
               
url = 'https://www.kuaidaili.com/free/intr/{}/' # 这是网站的 url
for i in range(1,10): # 爬取二十页
    time.sleep(1)  # 休息 1 秒
    get_one_parse(url.format(i))