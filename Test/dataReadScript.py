import os,cv2

def readData(path):
	X = []
	y = []
	for person in os.listdir(path):
		for sample in os.listdir(path+'/'+person):
			img = cv2.imread(path+'/'+person+'/'+sample)
			X.append(img)
			y.append(person)
	return X,y

if __name__ == '__main__':
	data,labels = readData('/home/jatin/Work/WatchDog/dataTraining')
	print(len(data),len(labels))