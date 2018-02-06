import cv2,numpy

def extractor(image,winSize):
	""" image is Numpy type submatrix from an photograph.
	winSize is an odd number for size of the patch.

	This returns a feature matrix with a vector of size 8 for each point i.e. matrix
	"""
	
	# Finding Harris's Intrest Points,	
	dst = cv2.cornerHarris(image,2,3,0.04)
	img=image.copy()
	img[dst>0.01*dst.max()]=0
	y,x = numpy.where(img==0)
	z=[x,y]
	z = numpy.array(z)
	z = numpy.transpose(z)
	p = [[dst[y,x],x,y] for x,y in z if x>1 and x<148 and y>1 and y<148]
	p.sort()
	z = [[x,y] for d,x,y in p[:50]]

	#Finding features at HIPs
	feature = []
	w = int(winSize/2)
	for x,y in z:	
		patch=image[y-w:y+w+1,x-w:x+w+1]
		matA=patch[:w+1,:w+1].copy()
		matB=patch[:w+1,w:].copy()
		matC=patch[w:,:w+1].copy()
		matD=patch[w:,w:].copy()
		vector=[]
		for j in [matA,matB,matC,matD]:
			vector.append(numpy.mean(j)/255)
			p = int(j.shape[0]/2)
			q = int(j.shape[1]/2)
			byte = 0
			for k in range(8):
				byte = byte + calNeighbour(j,p,q,k)*2**k
			vector.append(byte/255)
		feature.append(vector)
	return numpy.array(feature)

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
	print(extractor(img,5))
	import time
	time.sleep(3)
	cv2.destroyAllWindows()