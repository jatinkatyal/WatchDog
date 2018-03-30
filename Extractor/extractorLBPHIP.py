import cv2,numpy

def extractor(image,winSize):
	""" image is Numpy type submatrix from an photograph.
	winSize is an odd number for size of the patch.

	This returns a feature matrix with a vector of size 4 for each point i.e. matrix
	"""
	return None
	# Finding Harris's Intrest Points,	
	w = int(winSize/2)
	pad = [w,image.shape[0]-w-1,w,image.shape[1]-w-1]

	img=image[pad[0]:pad[1],pad[2]:pad[3]]
	dst = cv2.cornerHarris(img,2,3,0.04)
	img[dst>0.01*dst.max()]=0
	y,x = numpy.where(img==0)
	z=[x,y]

	z = numpy.array(z)
	z = numpy.transpose(z)
	p = [[dst[y,x],x,y] for x,y in z]
	p.sort()
	z = [[x,y] for d,x,y in p if x>int(winSize/2) and x<image.shape[1]-int(winSize/2) and y>int(winSize/2) and y<image.shape[0]-int(winSize/2)]
	if len(z)<10:
		print('less points')
		return None
	z=z[:10]

	#Finding features at HIPs
	vector=[]
	w = int(winSize/2)
	for x,y in z:	
			byte = 0
			for k in range(8):
				byte = byte + calNeighbour(image,x,y,k)*2**k
			vector.append(byte/255)
	return numpy.array(vector)

def calNeighbour(img,i,j,k):
	if i==0 and k<3:
		return 0
	if j==0 and k in [0,6,7]:
		return 0
	if j==img.shape[1]-1 and k in [2,3,4]:
		return 0
	if i==img.shape[0]-1 and k in [4,5,6]:
		return 0

	if k==0:
		if img[i-1,j-1]<img[i,j]:
			return 0
		else:
			return 1
	if k==1:
		if img[i-1,j]<img[i,j]:
			return 0
		else:
			return 1
	if k==2:
		if img[i-1,j+1]<img[i,j]:
			return 0
		else:
			return 1
	if k==3:
		if img[i,j+1]<img[i,j]:
			return 0
		else:
			return 1
	if k==4:
		if img[i+1,j+1]<img[i,j]:
			return 0
		else:
			return 1
	if k==5:
		if img[i+1,j]<img[i,j]:
			return 0
		else:
			return 1
	if k==6:
		if img[i+1,j-1]<img[i,j]:
			return 0
		else:
			return 1
	if k==7:
		if img[i,j-1]<img[i,j]:
			return 0
		else:
			return 1

if __name__ == '__main__':
	img = cv2.imread('test.jpg')
	img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	feature = extractor(img,5)
	print(len(feature),feature)
	import time
	time.sleep(3)
	cv2.destroyAllWindows()