'''http://www.pythonchallenge.com/pc/def/peak.html'''

import pickle
import urllib2

url5 = 'http://www.pythonchallenge.com/pc/def/banner.p'
req5 = urllib2.Request(url5)
ct5 = urllib2.urlopen(req5).read()
tmp5 = pickle.loads(ct5)
print tmp5

def translate5(v):
	r =[]
	for k in v:
		if type(k) == tuple :
			r.append(chr(ord(k[0]) + k[1]))
		else:
			r.append(translate5(k))
	return r

def translate5_2(v):
	r = []
	for k in v:
		if type(k) == tuple:
			print k[0],k[1]
		else:
			print '\n'
			translate5_2(k)

def translate5_3(v):
	for k in v:
		r = ''
		for k1 in k:
			for k3 in range(k1[1]):
				r += k1[0]
		print r
		#print '\n'
#print translate5(tmp5)
#print translate5_2(tmp5)
print translate5_3(tmp5)
