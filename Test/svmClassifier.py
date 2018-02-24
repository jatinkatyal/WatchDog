from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.utils import resample
import numpy

#prep data
data = numpy.genfromtxt('data_uci.csv',delimiter=',')
X = data[:,:-2]
y = data[:,-1]
X,y = resample(X,y,random_state=0)

#classify
clf = SVC(gamma=0.001)
kf = KFold(n_splits=7,shuffle=True)
scores=[]
for train,test in kf.split(X):
	trainX = X[train]
	trainY = y[train]
	testX = X[test]
	testY = y[test]
	clf.fit(trainX,trainY)
	scores.append(clf.score(testX,testY))
scores = numpy.array(scores)
print(scores.mean())