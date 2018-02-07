from sklearn import tree
import numpy
X = numpy.genfromtxt('/home/jatin/Work/WatchDog/features.csv',delimiter=',')
y = numpy.genfromtxt('/home/jatin/Work/WatchDog/classes.csv',delimiter=',')

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

testX = numpy.genfromtxt('/home/jatin/Work/WatchDog/featuresToTest.csv',delimiter=',')
testy = numpy.genfromtxt('/home/jatin/Work/WatchDog/classesToTest.csv',delimiter=',')

count = 0
for i in range(len(testX)):
	pred = clf.predict([testX[i]])
	if pred == testy[i]:
		count+=1
print(count)