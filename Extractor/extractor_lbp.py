import cv2,numpy,time

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

def extractor(image):
	lbpImg = numpy.zeros(image.shape)
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			byte=0
			for k in range(8):
				byte = byte + calNeighbour(image,i,j,k)*2**k
			lbpImg[i,j]=byte
	return lbpImg.flatten()

if __name__=='__main__':
	img = cv2.imread('test.jpg')
	img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
	feature = extractorLBP(img)
	cv2.imshow('lbp',feature)
	cv2.waitKey(10000)