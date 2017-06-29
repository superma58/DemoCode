'''http://www.pythonchallenge.com/pc/def/channel.html'''
# 6

import os,sys
import re
import urllib2
import zipfile


def getNothingValue(value):
	path = '6\\'+ str(value) + '.txt'
	f = open(path, 'r')
	ct4 = f.read()
	f.close()
	print 'next:',ct4
	if ct4.find('nothing') < 0:
		print ct4
		return
	re4Num = re.compile(r'[0-9]+')
	frontIdex = ct4.find('nothing is')
	newCt4 = ct4[frontIdex:]
	value = re4Num.findall(newCt4)[0]
	getNothingValue(value)

#getNothingValue(90052)

'''
next: Next nothing is 46145
next: Collect the comments.
Collect the comments.'''

#--------------step 2
f = zipfile.ZipFile(os.path.join(os.getcwd() + '')   'C:\Users\ERENQMA\Desktop\New folder/6/channel.zip')
zipInfoList = f.infolist()
print zipInfoList
for info in zipInfoList:
	print info.comments




#addition
import urllib2 as ul2
import cookielib as cl

def printCookie(url):
	cookie = cl.CookieJar()
	handle = ul2.HTTPCookieProcessor(cookie)
	opener = ul2.build_opener(handle)
	response = opener.open(url)
	text = response.read()

	print 'result:', text
    #print 'cookie:'
	for item in cookie:
		print 'name:' + item.name + '-value:' + item.value

printCookie('http://www.pythonchallenge.com/pc/def/hockey.html')



