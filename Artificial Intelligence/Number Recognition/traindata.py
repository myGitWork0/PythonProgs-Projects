import numpy as np
import matplotlib.pyplot as pt
import pandas as pd

#from sklearn.tree import DecisionTreeClassifier

from sklearn.neural_network import MLPClassifier

data=pd.read_csv("training.csv").as_matrix()
#clf=DecisionTreeClassifier()

clf=MLPClassifier(activation='logistic',hidden_layer_sizes=(64, 64), max_iter=800, alpha=1e-4,solver='sgd',learning_rate_init=.1)
xtrain=data[0:,0:64]
train_label=data[0:,64]
clf.fit(xtrain,train_label)

data1=pd.read_csv("testing.csv").as_matrix()

xtest=data1[0:,0:64]

actual_label=data1[0:,64]

d=xtest[9]

d.shape=(8,8)

pt.imshow(255-d,cmap='gray')
print("The predicted shape is : ")
print(clf.predict([xtest[9]]))

print("Guess and tally with the image")

pt.show()



p=clf.predict(xtest)

count=0
for i in range(0,1796):
	if p[i]==actual_label[i] :
		count=count+1
	else :
		0
print("Accuracy of the test data set is = ",(count/1796)*100)


