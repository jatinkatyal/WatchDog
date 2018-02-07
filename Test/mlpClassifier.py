from sklearn.neural_network import MLPClassifier
import numpy,time
X = numpy.genfromtxt('/home/jatin/Work/WatchDog/features.csv',delimiter=',')
y = numpy.genfromtxt('/home/jatin/Work/WatchDog/classes.csv',delimiter=',')

clf = MLPClassifier(max_iter=1000)
clf = clf.fit(X,y)
testX = numpy.genfromtxt('/home/jatin/Work/WatchDog/featuresToTest.csv',delimiter=',')
testy = numpy.genfromtxt('/home/jatin/Work/WatchDog/classesToTest.csv',delimiter=',')

corrects = []
for i in range(len(testX)):
	pred = clf.predict([testX[i]])
	if pred == testy[i]:
		corrects.append(i)
print(corrects,len(corrects))