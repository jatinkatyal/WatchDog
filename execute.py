import cv2,time

from Eye.eye import Eye
from DnPP.detector import Detector
import Extractor.extractor_lbp as ext
#from DnPP import preprocesses

cam1 = Eye()
frame = cam1.see()
cv2.imshow('cam1',frame)
cv2.waitKey(50)

det = Detector()
faces = det.detect(frame)
features = []
for face in faces:
	cv2.imshow('face',face)
	cv2.waitKey(50)

	features.append(ext.extractorLBP(face))
for i in features:
	cv2.imshow('LBP face',i)
	cv2.imwrite('features of subject: '+str(features.index(i))+'.jpg',i)
	cv2.waitKey(50)

print('done')
time.sleep(5)
cv2.destroyAllWindows()