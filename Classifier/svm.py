from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.utils import resample
import numpy

def classify(data,labels):
	X = data
	y = labels
	X,y = resample(X,y,random_state=0)

	#classify
	print('Using SVM, K Fold cross validation')
	clf = SVC(gamma=0.001)
	kf = KFold(n_splits=7,shuffle=True)
	scores=[]
	count=0
	for train,test in kf.split(X):
		count+=1
		trainX = X[train]
		trainY = y[train]
		testX = X[test]
		testY = y[test]
		clf.fit(trainX,trainY)
		score = clf.score(testX,testY)
		print('fold ',count,' : ',score)
		scores.append(score)
	scores = numpy.array(scores)
	return scores.mean(),clf