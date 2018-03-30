from cv2 import cvtColor,COLOR_RGB2GRAY,equalizeHist,imread
from numpy import array,where
from os import listdir
from pickle import dump,load
#---Created Modules---
from Eye.eye import Eye
from DnPP.detector import Detector
#Extractors
import Extractor.extractor_lbp as lbp
import Extractor.extractorGLCM as glcm
import Extractor.extractorGLCMHIP as glcmhip
#Classifiers
import Classifier.decisionTree as dtree
import Classifier.svm as svm

#Prepare data
def prepData(path):
	cam = Eye()
	det = Detector()
	faces = []
	labels = []
	print('Reading data...')
	for person in listdir(path):
		for sample in listdir(path+'/'+person):	
			#capture image
			frame = cam.see(path+'/'+person+'/'+sample)
			#detect face
			newFaces = det.detect(frame)
			if newFaces:
				for face in newFaces:
					faces.append(face)
					labels.append(int(person))
	return faces,labels

#Train
def train(ext,clf):
	file = open('Models/'+ext+'-'+clf+'.mod','wb')
	faces, y = prepData('Training data')
	print('Extracting features...')
	X = []
	if ext=='LBP':
		for face in faces:
			X.append(lbp.extractor(face))
	elif ext=='GLCM':
		for face in faces:
			X.append(glcm.extractor(face))
	elif ext=='GLCMHIP':
		i=0
		for face in faces:
			ret,feature = glcmhip.extractor(face,55)
			if ret:
				X.append(feature)
				i+=1
			else:
				y.pop(i)
	else:
		print('Invalid extractor in train function')
		exit(0)
	X = array(X)
	y=array(y)
	print(X.shape)
	print('Training model on extracted data...')
	if clf == 'DTree':
		score,clf = dtree.classify(X,y)
		print('Performance score: ',score)
	elif clf == 'SVM':
		score,clf = svm.classify(X,y)
	else:
		print('Invalid classifier in train function.')
		exit(0)
	#save model
	print('Saving new model...')
	dump(clf, file)
	file.close()
	print('Operation completed.')

def use(ext,clf,img):
	file = ext+'-'+clf+'.mod'
	if file in listdir('Models'):
		print('Model found, loading...')
		file = open('Models/'+file,'rb')
		model = load(file)
		file.close()
		print('Model loaded.')
		
		det = Detector()
		face = det.detect(img)[0]
		print('Face detected.')
		if ext=='LBP':
			features = lbp.extractor(face)
		elif ext=='GLCM':
			features = glcm.extractor(face)
		elif ext=='GLCMHIP':
			ret,features = glcmhip.extractor(face,55)
			if not ret:
				print("Feature extraction didn't complete, select different input.")
				return None
		print('Features extracted.')
		p = model.predict([features])
		print('Prediction: ',p)
		return p
	else:
		print('Specified model not found.')

#Menu
def menu():
	print('Hello, what would you like to do?')
	print('1. Train')
	print('2. Use')
	print('3. Exit')
	choice = int(input('Enter your choice: '))
	return choice

if __name__ == '__main__':
	#Make a selection
	choice = menu()
	while choice:
		if choice==1:
			print('Select an Extractor.')
			print('1. Linear Binary Patterns.')
			print('2. Gray Level Covarriance Matrix')
			print('3. Gray Level Covarriance Matrix features at Harris Interest Points')
			choice = int(input('Your choice: '))
			if choice == 1:
				ext = 'LBP'
			elif choice == 2:
				ext = 'GLCM'
			elif choice == 3:
				ext = 'GLCMHIP'

			print('Select a Classifier.')
			print('1. Support Vector Machine')
			print('2. Decission Tree')
			choice = int(input('Your choice: '))
			if choice == 1:
				clf = 'SVM'
			elif choice == 2:
				clf = 'DTree'

			print('Training new model...')
			train(ext,clf)

		elif choice==2:
			print('Select an Extractor.')
			print('1. Linear Binary Patterns.')
			print('2. Gray Level Covarriance Matrix')
			print('3. Gray Level Covarriance Matrix features at Harris Interest Points')
			choice = int(input('Your choice: '))
			if choice == 1:
				ext = 'LBP'
			elif choice == 2:
				ext = 'GLCM'
			elif choice == 3:
				ext = 'GLCMHIP'

			print('Select a Classifier.')
			print('1. Support Vector Machine')
			print('2. Decission Tree')
			choice = int(input('Your choice: '))
			if choice == 1:
				clf = 'SVM'
			elif choice == 2:
				clf = 'DTree'
			img = imread('Training data/3/3_0.jpg')
			use(ext,clf,img)

		elif choice==3:
			exit(0)
		else:
			print('Invalid choice selected, please try again.')
		choice = menu()