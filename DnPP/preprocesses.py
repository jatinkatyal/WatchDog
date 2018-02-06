"""Functions for preprocessing image"""
import cv2

def toGray(frame):
	return cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

def rescale(frame):
	return cv2.resize(frame,(150,150))

def equalize(frame):
	return cv2.equalizeHist(frame)

def detectorPP(frame):
	frame = toGray(frame)
	return equalize(frame)

if __name__=='__main__':
	frame= cv2.imread('test.jpg')
	cv2.imshow('test',toGray(frame))
	cv2.waitKey(500)