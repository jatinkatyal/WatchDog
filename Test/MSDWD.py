import cv2,numpy

def extractorRPDMSD(image,num,winSize):
	""" image is Numpy type submatrix from an photograph.
	num is number of points from which features are to be extracted.
	winSize is an odd number for size of the patch.

	This returns a feature matrix with a vector of size 8 for each point i.e. (num X 8) matrix
	"""
	feature = []
	for i in range(num):
		x=numpy.random.randint((winSize-1)/2,image.shape[0]-(winSize-1)/2)
		y=numpy.random.randint((winSize-1)/2,image.shape[1]-(winSize-1)/2)
		d=int(winSize/2)
		patch=image[x-d:x+d+1,y-d:y+d+1]
		print(patch)
		matA=patch[0:d+1,0:d+1].copy()
		matB=patch[0:d+1,d:].copy()
		matC=patch[d:,0:d+1].copy()
		matD=patch[d:,d:].copy()
		a = abs(matA-matB)
		b = abs(matC-matD)
		c = abs(matA-matC)
		d = abs(matB-matD)
		vector=[]
		for j in [a,b,c,d]:
			vector.append(numpy.mean(j))
			vector.append(numpy.std(j))
		feature.append(vector)
	return feature

if __name__=='__main__':
	file = input('file name: ')
	img = cv2.imread(file)
	img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	print(extractorRPDMSD(img,8,3))