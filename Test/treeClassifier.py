from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.utils import resample
import numpy

#prep data
data = numpy.genfromtxt('/home/jatin/Work/WatchDog/Test/data.csv',delimiter=',')
X = data[:,:-2]
y = data[:,-1]
X,y = resample(X,y,random_state=0)

#classify
clf = DecisionTreeClassifier()
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