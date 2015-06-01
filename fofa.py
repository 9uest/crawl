#!/usr/bin/python

import base64
import urllib2
import json
import re
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def Sofa_Search(keywords):
	keywords = base64.b64encode(keywords)
	search = "http://fofa.so/api/result?qbase64=%s&key=d69f306296e8ca95fded42970400ad23&email=her0m@qq.com" %keywords
	urls = urllib2.urlopen(search).read()
	urllist = json.loads(urls)
	urllist = urllist.get('results')
	Pyload(urllist)


def Pyload(urllist):
	Pyload1 = "phpinfo.php"
	Existurl = []
	for i in urllist:
		if not regex.findall(i):
			i = "http://"+i
			i = i+"/"+Pyload1
			#print "Test %s" %i
			try:
				data = urllib2.urlopen(i,timeout=1)
				if data.getcode() == 200:
					print  "[+]%s exist!!" %(i)
					Existurl.append(i)
					break
				else:
					print "[-]" + i + "   Error CODE = %s" %data.getcode()
			except:
				print "[-]" + i + "   Time out"
	print  Existurl
	print "Test Over"
	#print existurl

def main():
	Sofa_Search("phpinfo.php")


if __name__ == '__main__':

	main()