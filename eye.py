import cv2

class Eye(object):
	"""Eyes sees everything"""
	def __init__(self):
		self.cam = cv2.VideoCapture(0)

	def see(self):
		ret,frame = self.cam.read()
		try:
			if ret:
				return frame
		except:
			print("Error reading image in eye")

if __name__=='__main__':
	cam1 = Eye()
	for i in range(30):
		cv2.imshow('img',cam1.see())
		cv2.waitKey(100)
	cam1.cam.release()
	cv2.destroyAllWindows()