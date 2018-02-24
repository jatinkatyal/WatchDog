import numpy
from keras.models import Sequential
from keras.layers import  Activation, Conv1D, Dense, Dropout, MaxPooling1D
from keras.utils import to_categorical
from sklearn.utils import resample
from sklearn.model_selection import KFold
#load data
data = numpy.genfromtxt('features.csv',delimiter=',')
X = data[:,:-1]
y = data[:,-1]-1
print(X.shape,y.shape)
# OR
#X = numpy.genfromtxt('data_uci.csv',delimiter=',')
#y = numpy.genfromtxt('final_y_train.txt',delimiter=',')
#X,y = resample(X,y,random_state=0)
n=len(set(y))+1
y = to_categorical(y,num_classes=n)

kf = KFold(shuffle=True,n_splits=10)
scores=[]
count = 0
for train,test in kf.split(X,y):
	print('fold: ',count)
	count+=1
	model = Sequential()
	model.add(Dense(X.shape[1],input_shape=(X.shape[1],)))
	model.add(Activation('relu'))
	model.add(Dense(25))
	model.add(Activation('relu'))
	model.add(Dense(100))
	model.add(Activation('relu'))
	model.add(Dense(25))
	model.add(Activation('relu'))
	model.add(Dropout(0.01))
	model.add(Dense(n))
	model.add(Activation('softmax'))

	model.compile(optimizer='SGD',loss='categorical_crossentropy',metrics=['accuracy'])

	model.fit(X[train],y[train],epochs=10,verbose=0)

	score = model.evaluate(X[test],y[test])
	scores.append(score[1]*100)
	print(score)
scores = numpy.array(scores)
print(scores.mean())