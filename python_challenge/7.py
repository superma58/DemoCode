'''http://www.pythonchallenge.com/pc/def/oxygen.html'''

from PIL import Image
import numpy as np

img = np.array(Image('./7/oxygen.jpg'))

value = []
px = 0
linePic = img[45][0:608]
for v in range(0, 608 ,7):
	value.append(linePic[v][1])

strValue = ''
for v in value:
	strValue += chr(v)

print strValue   #smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

strValue = ''
for v in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
	strValue += chr(v)

print strValue  #integrity


