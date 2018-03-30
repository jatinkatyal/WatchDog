'''
This script uses a detector from DnPP to detect faces and
extract features using an extractor from Extractor over
training data in directory called 'faceImages'. Extracted
features are stored in features.csv and respective classes
are in classes.csv.
'''

I = 4 #This is the class of training examples in faceImages directory.

import cv2,time,numpy,os
from Eye.eye import Eye
from DnPP.detector import Detector
from DnPP import preprocesses as PP
#import Extractor.extractor_lbp as ext
#import Extractor.extractorHIPMSDWD as ext
#import Extractor.extractorMeanWindowsAtHIP as ext
#import Extractor.extractorMLBPWHIP as ext
#import Extractor.extractorLBPHIP as ext
import Extractor.extractorGLCMHIP as ext
#import Extractor.extractorGLCM as ext
#from Classifier.svm import classify
from Classifier.decisionTree import classify

#Load data
cam1 = Eye()
det = Detector()
faces = []
labels = []
features = []
for person in os.listdir('Training data'):
	for sample in os.listdir('Training data/'+person):	
		#capture image
		frame = cam1.see('Training data/'+person+'/'+sample)
		print('Reading: '+sample+' from '+person)

		#detect face
		newFaces = det.detect(frame)
		if newFaces:
			print('Detected: '+str(len(newFaces)))
			for face in newFaces:
				faces.append(face)
				#extract features
				cv2.imshow(person,face)
				ret,feature = ext.extractor(face,25)
				#feature = numpy.hstack([feature,int(person)])
				if ret:
					features.append(feature)
					labels.append(int(person))
cam1.closeEye()

#save features
features = numpy.array(features)
labels = numpy.array(labels)
print(features.shape)
numpy.savetxt('Extracted data/data.csv',features,fmt='%10.5f',delimiter=',')
print('Features saved to data.csv')

#classify
print('Using cross validation')
print('Score: ',classify(features,labels)[0])
#cv2.destroyAllWindows()