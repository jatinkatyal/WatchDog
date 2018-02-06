'''
This script uses a detector from DnPP to detect faces and
extract features using an extractor from Extractor over
training data in directory called 'faceImages'. Extracted
features are stored in features.csv and respective classes
are in classes.csv.
'''

I = 1 #This is the class of training examples in faceImages directory.

import cv2,time,numpy,os
from Eye.eye import Eye
from DnPP.detector import Detector
#import Extractor.extractor_lbp as ext
import Extractor.extractorHIPMSDWD as ext
from DnPP import preprocesses as PP

cam1 = Eye()
det = Detector()
faces = []
for image in os.listdir('faceImages'):
	#capture image
	frame = cam1.see('faceImages/'+image)
	cv2.imshow('cam1',frame)
	cv2.waitKey(50)

	#detect face
	newFaces = det.detect(frame)
	if newFaces:
		for face in newFaces:
			faces.append(face)

#extract features
features = []
for face in faces:
	cv2.imshow('face',face)
	cv2.waitKey(50)
	features.append(ext.extractor(PP.toGray(face),5))

#display features
for p in features:
	y = numpy.ones((p.shape[0],1))*I
	f1 = open('features.csv','ab')
	f2 = open('classes.csv','ab')
	numpy.savetxt(f1,p,delimiter=',')
	numpy.savetxt(f2,y,delimiter=',')
	f1.close()
	f2.close()
image = faces.pop(0)
for face in faces:
	image = numpy.hstack([image,face])
print(len(faces))
cv2.imwrite(str(I)+'.jpg',image)
print('done')
time.sleep(5)
cv2.destroyAllWindows()