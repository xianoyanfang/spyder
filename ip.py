# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:37:46 2017

@author: xiao
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import time

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent
# 获取ip存储到数组a中
url = 'http://www.xicidaili.com/nn/1'
req = requests.get(url,headers=header)
res = urllib2.urlopen(req).read()

soup = BeautifulSoup(req.text)
ips = soup.findAll('tr')
f = open("../src/proxy","w")
a = []
for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    ip_temp = tds[1].text+":"+tds[2].text
    print(ip_temp+'\n')
    a.append(ip_temp)

# 这里可以加入列表存储可访问ip ，但是下面并没有只是简单的print
url = "http://ip.chinaz.com/getip.aspx"
for i in a:
    proxiy = {}
    pro = 'http://'+i
    proxiy['http'] = pro
    session = requests.Session()
    try:
        req = session.get(url,headers = header,proxies = proxiy)
        print(i)
    except:
        ;
    time.sleep(1)
    