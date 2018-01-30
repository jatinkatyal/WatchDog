import cv2,os
from . import preprocesses as PP
class Detector:
	"""Detects face using OpenCV & Haars."""
	def __init__(self):
		d = os.path.dirname(os.path.realpath(__file__))
		self.detector = cv2.CascadeClassifier(d+'/haarcascade_frontalface_default.xml')

	def detect(self,frame):
		img = PP.detectorPP(frame)
		faceCoords = self.detector.detectMultiScale(img,scaleFactor=1.1,minNeighbors=5)
		faces =[]
		for x,y,w,h in faceCoords:
			faces.append(frame[y:y+h,x:x+w])
		if len(faces)<1:
			return None
		return faces

if __name__=='__main__':
	frame = cv2.imread('test.jpg')
	d = detector()
	fs = d.detect(frame)
	if fs:
		print('found: '+str(len(fs)))
		for i in fs:
			cv2.imshow('subject: '+str(fs.index(i)),PP.rescale(i))
		cv2.waitKey(2000)
		cv2.destroyAllWindows()