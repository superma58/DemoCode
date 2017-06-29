import re
import urllib2

def getNothingValue(value):
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(value)
	ct4 = urllib2.urlopen(url).read()
	print 'next:',ct4
	if ct4.find('next nothing') < 0:
		print ct4
		return
	re4Num = re.compile(r'[0-9]+')
	frontIdex = ct4.find('next nothing is')
	newCt4 = ct4[frontIdex:]
	value = re4Num.findall(newCt4)[0]
	getNothingValue(value)

#getNothingValue(12345)

'''http://www.pythonchallenge.com/pc/def/linkedlist.php'''

#getNothingValue(8022)
'''
next: and the next nothing is 49574
next: and the next nothing is 82682
next: There maybe misleading numbers in the 
text. One example is 82683. Look only for the next nothing and the next nothing is 63579
next: You've been misleaded to here. Go to previous 
one and check.
'''

getNothingValue(63579)

'peak.html'