
def oddline(arr):
	arrTmp = arr.copy()
	for i in range(1,len(arrTmp),2):
		for k in range(0,len(arrTmp[i])):
			arrTmp[i][k] = [0,0,0]
	return 

def oddcol(arr):
	arrTmp = arr.copy()
	for i in range(0,len(arrTmp)):
		for k in range(0,len(arrTmp[i]),2):
			arrTmp[i][k] = [0,0,0]
	return arrTmp

def evenline(arr):
	arrTmp = arr.copy()
	for i in range(0,len(arrTmp),2):
		for k in range(0,len(arrTmp[i])):
			arrTmp[i][k] = [0,0,0]
	return arrTmp

def evencol(arr):
	arrTmp = arr.copy()
	for i in range(0,len(arrTmp)):
		for k in range(1,len(arrTmp[i]),2):
			arrTmp[i][k] = [0,0,0]
	return arrTmp


def scale(arr):
	arrTmp = arr.copy()
	for i in range(0,len(arrTmp)-2,2):
		for k in range(0,len(arrTmp[i])-2,2):
			arrTmp[i][k] = arrTmp[i][k+1]
		for k in range(1,len(arrTmp[i+1])-2,2):
			arrTmp[i+1][k] = arrTmp[i+1][k+1]
	return arrTmp
arr113=scale(arr112)

def scale2(arr):
	arrTmp = arr.copy()
	for i in range(0,len(arr)):
		if i % 2 == 0:
			for k in range(1,len(arr[i]),2):
				arrTmp[i][k] = [0,0,0]
		else:
			for k in range(0,len(arr[i]),2):
				arrTmp[i][k] = [0,0,0]
	return arrTmp


def scale3(arr):
	arrTmp = arr.copy()
	for i in range(0,len(arr)):
		if i % 2 != 0:
			for k in range(1,len(arr[i]),2):
				arrTmp[i][k] = [0,0,0]
		else:
			for k in range(0,len(arr[i]),2):
				arrTmp[i][k] = [0,0,0]
	return arrTmp

#def odd(arr, k)

#right:
arr113=scale2(arr111)
Image.fromarray(np.array(arr113)).show()

#result:
#picture show:evil