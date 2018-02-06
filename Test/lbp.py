import cv2, numpy

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
path = input('file: ')
img = cv2.imread(path)
img = cv2.resize(img,(480,320))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lbp = numpy.zeros(img.shape)
cv2.imshow('img',img)
cv2.waitKey(50)
print('finding LBP')
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		byte=0
		for k in range(8):
			byte = byte + calNeighbour(img,i,j,k)*2**k
		lbp[i,j]=byte
cv2.imwrite('lbp.jpg',lbp)
cv2.imshow('lbp',lbp)
cv2.waitKey(1000)
#cv2.destroyAllWindows()
