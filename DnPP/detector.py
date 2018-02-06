import cv2,os
from . import preprocesses as PP
class Detector:
	"""Detects face using OpenCV & Haars."""
	def __init__(self):
		d = os.path.dirname(os.path.realpath(__file__))
		self.faceDetector = cv2.CascadeClassifier(d+'/haarcascade_frontalface_default.xml')
		self.leftEyeDetector = cv2.CascadeClassifier(d+'/haarcascade_lefteye_2splits.xml')
		self.rightEyeDetector = cv2.CascadeClassifier(d+'/haarcascade_righteye_2splits.xml')

	def detect(self,frame):
		img = PP.detectorPP(frame)
		faceCoords = self.faceDetector.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)
		faces =[]
		for x,y,w,h in faceCoords:
			face = frame[y:y+h,x:x+w]
			if self.detectEyes(face):
				faces.append(PP.rescale(face))
		if len(faces)<1:
			return None
		return faces
	
	def detectEyes(self,face):
		leftEye = self.leftEyeDetector.detectMultiScale(PP.toGray(face),scaleFactor=1.1,minNeighbors=5)
		rightEye = self.rightEyeDetector.detectMultiScale(PP.toGray(face),scaleFactor=1.1,minNeighbors=5)
		if len(leftEye)>0 and len(rightEye)>0:
			return True
		return False

if __name__=='__main__':
	import time

	frame = cv2.imread('test.jpg')
	d = Detector()
	fs = d.detect(frame)
	if fs:
		print('found: '+str(len(fs)))
		for i in fs:
			print(i)
			cv2.imshow('subject',i)
			cv2.waitKey(50)
			time.sleep(2)
		cv2.destroyAllWindows()