#!/usrl/bin/python
#-*-coding=utf8-*-

import urllib2
import  re,time,os
import threading
from bs4 import BeautifulSoup
from multiprocessing import Process,Pool


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
	print "Run Process %s" %os.getpid()
	print Baiduurl
	html = urllib2.urlopen(Baiduurl).read()
	#print html
	soup = BeautifulSoup(html)
	urllist = []
	print ("[+]Extraction of Page...") 
	for link in soup.find_all('a'):
		i = link.get('href')
		try:
			if regex.findall(i):
				print "Open %s" %i
				url = urllib2.urlopen(i,timeout=1).geturl()
				urllist.append(url)
				print  url
		except:
			pass
	return urllist
#def main():
	# threadings  = []
	# for i in xrange(2):
	# 	url = BaiduUrl('test',i)
	# 	threads = threading.Thread(target=BaiduSearch,args=url)
	# 	threadings.append(threads)
	# return threadings
	
if  __name__ == "__main__":
	# url1,url2 = BaiduUrl('test',1),BaiduUrl('python',1)
	# url =[url1,url2]
	print "Process pid is %s" %(os.getpid())
	p = Pool()
	for i in range(1,3):
		url = BaiduUrl('python',i)
		p.apply_async(BaiduSearch,args=(url,))
		# BaiduSearch(url).urllist
		# print("[+]Data to repeat...")
		# urllist = list(set(urllist))
		# f = os.open("url.txt",wa)
		# f.write(urllist)
		# f.close
		# print("Every ok. export in [url.txt]")
		# time.sleep(1)
	print "[+]Waiting for all process.."
	p.close()
	p.join()
	print "Process End!!! Good lock!"
	# for i in main():
	# 	i.setDaemon(True)
	# 	i.start()
	# i.join()



# rehtml = re.findall('<a href="(.*?)"',html,re.S)
# for i in  rehtml:
# 	if regex.findall(i):
# 		print urllib2.urlopen(i).geturl()
