import cv2

class Eye:
	"""Eyes sees everything, captures form camera by default if scene is not provided."""
	def __init__(self,path=None):
		self.path = path
		self.cam = cv2.VideoCapture(0)

	def see(self):
		if self.path:
			try:
				frame = cv2.imread(self.path)
			except:
				print('Error reading file through eye.')
		else:
			try:
				ret,frame = self.cam.read()
			except:
				print("Error capturing image in eye")
		cv2.waitKey(50)
		return frame

	def closeEye(self):
		self.cam.release()

if __name__=='__main__':
	cam1 = Eye('test.jpg')
	for i in range(30):
		cv2.imshow('img',cam1.see())
	cam1.closeEye()
	cv2.destroyAllWindows()