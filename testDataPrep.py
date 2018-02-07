'''
This script uses a detector from DnPP to detect faces and
extract features using an extractor from Extractor over
training data in directory called 'faceImages'. Extracted
features are stored in featuresToTest.csv and respective classes
are in classesToTest.csv.
'''

import cv2,time,numpy,os
from Eye.eye import Eye
from DnPP.detector import Detector
#import Extractor.extractor_lbp as ext
#import Extractor.extractorHIPMSDWD as ext
#import Extractor.extractorMeanWindowsAtHIP as ext
#import Extractor.extractorMLBPWHIP as ext
import Extractor.extractorLBPWHIP as ext
from DnPP import preprocesses as PP

cam1 = Eye()
det = Detector()
faces = []
labels = []
features = []
for person in os.listdir('dataProbe'):
	for sample in os.listdir('dataProbe/'+person):	
		#capture image
		frame = cam1.see('dataProbe/'+person+'/'+sample)
		print('Reading: '+sample+' from '+person)
		#cv2.imshow('cam1',frame)
		#cv2.waitKey(50)

		#detect face
		newFaces = det.detect(frame)
		if newFaces:
			print('Detected: '+str(len(newFaces)))
			for face in newFaces:
				faces.append(face)
				labels.append(int(person))
				#extract features
				#cv2.imshow(person,face)
				features.append(ext.extractor(PP.toGray(face),5))
cam1.closeEye()				
print(len(faces),len(features),len(labels))
#save features
numpy.savetxt('classesToTest.csv',labels,delimiter=',')
numpy.savetxt('featuresToTest.csv',features,delimiter=',')

print('done')
cv2.destroyAllWindows()