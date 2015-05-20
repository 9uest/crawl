#!/bin/python
# -*-coding=utf8-*-

import urllib2
import re
import time
import threading
from bs4 import BeautifulSoup



regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def BaiduUrl(world,n):
        Search = "http://baidu.com/s?wd=%s&pn=%s" %(world,n*10)
        return Search
def BaiduSearch(Baiduurl):	
        html = urllib2.urlopen(Baiduurl).read()
        # print html
        soup = BeautifulSoup(html)
        urllist = []
        print ("[+]Extraction of Page...")
        for link in soup.find_all('a'):
            i = link.get('href')
            try:
                if regex.findall(i):
                    url = urllib2.urlopen(i,timeout=1).geturl()
                    urllist.append(url)
                    print  url
            except:
                pass
        print("[+]Data to repeat...")
        urllist = list(set(urllist))
        print("Every ok")
        time.sleep(1)
        return
def main():
        threadings  = []
        for i in xrange(2):
            url = BaiduUrl('test',i)
            threads = threading.Thread(target=BaiduSearch(url))
            threadings.append(threads)
        return threadings
if  __name__ == "__main__":
        for i in main():
            i.setDaemon(True)
            i.start()



# rehtml = re.findall('<a href="(.*?)"',html,re.S)
# for i in  rehtml:
# 	if regex.findall(i):
# 		print urllib2.urlopen(i).geturl()
