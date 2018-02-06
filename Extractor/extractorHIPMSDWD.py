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
		a = abs(matA-matB)
		b = abs(matC-matD)
		c = abs(matA-matC)
		d = abs(matB-matD)
		vector=[]
		for j in [a,b,c,d]:
			vector.append(numpy.mean(j))
			vector.append(numpy.std(j))
		feature.append(vector)
	return numpy.array(feature)

if __name__ == '__main__':
	img = cv2.imread('test.jpg')
	img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	extractor(img,5)
	import time
	time.sleep(3)
	cv2.destroyAllWindows()