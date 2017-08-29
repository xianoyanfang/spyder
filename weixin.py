# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import random
def yd_weixin(url,str1):# url ±ØÐëÎªÒ»¸öÁÐ±í,str1¿ÉÒÔÊÇÒª²éÕÒµÄÁ´½Ó
    targeturl = []
    user_agent = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                  'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
                  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'];
    ip = ['42.159.242.36:808','210.26.54.43:808','101.201.234.108:808','112.123.40.54:9745','58.241.231.99:8118',
      '114.221.0.64:8118','121.237.6.20:8118','42.227.191.15:8118','221.8.172.82:80','113.124.94.189:808']
    accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    header = {}
    header['Accept'] = accept
    proxiy = {'http':'http://'+ip[random.randint(0,9)]}
    # ¶ÔÓÚ´óÁ¿Êý¾Ý¼¯¿ÉÒÔ¼ÓÈëÒ»¸öÑ­»·
    header['User_Agent'] = user_agent[random.randint(0,3)]
    session = requests.Session()
    for i in url:
        req = session.get(i,headers = header,proxies = proxiy)
        bsObj = BeautifulSoup(req.text)
        # ÅÐ¶Ï¸ÃÁ´½Ó±êÌâÊÇ·ñ³öÏÖ¿í´ø
        if str1 in bsObj.div.get_text():
            targeturl.append(i)
    return targeturl
if __name__ == '__main__':
    url = ['https://mp.weixin.qq.com/s?__biz=MjM5MjQ1NzE2MA==&mid=2678597408&idx=2&sn=cd4158336b6e240383b35c6cad6b2810&chksm=bcfa8f878b8d0691e8e93d9404792ad957d3f393150962f98fd6e414d74c2db6f36dff6e97e9&mpshare=1&scene=1&srcid=0829hJWs0axepmKrnlE2bZA3&pass_ticket=jE0aWocyIE1nqUM8O5hun4sFN6pWZr3cUGGgG5YmHo5KRLYF%2F%2BlBd4CudMr8L7xn#rd']
    target_url =yd_weixin(url,'宽带')
    print(target_url)