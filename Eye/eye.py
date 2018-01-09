import cv2

class Eye(object):
	"""Eyes sees everything"""
	def __init__(self):
		self.cam = cv2.VideoCapture(0)

	def see(self):
		ret,frame = self.cam.read()
		try:
			if ret:
				cv2.waitKey(70)
				return frame
		except:
			print("Error reading image in eye")

	def closeEye(self):
		self.cam.release()

if __name__=='__main__':
	cam1 = Eye()
	for i in range(30):
		cv2.imshow('img',cam1.see())
	cam1.closeEye()
	cv2.destroyAllWindows()