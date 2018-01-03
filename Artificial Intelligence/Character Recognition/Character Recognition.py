import numpy as np
import matplotlib.pyplot as pt
import pandas as pd

from sklearn.neural_network import MLPClassifier

data=pd.read_csv("data.csv").as_matrix()


clf=MLPClassifier(activation='logistic',hidden_layer_sizes=(16, 16), max_iter=800, alpha=1e-4,solver='sgd',learning_rate_init=.1)
xtrain=data[0:16000,1:17]
train_label=data[0:16000,0]
clf.fit(xtrain,train_label)

data1=pd.read_csv("data.csv").as_matrix()

xtest=data1[16001:,1:17]

actual_label=data1[16001:,0]

d=xtest[50]

d.shape=(4,4)

#pt.imshow(255,cmap='gray')
print("The predicted letter is : ")
print(clf.predict([xtrain[0]]))


pt.show()



p=clf.predict(xtest)

count=0
for i in range(0,1796):
	if p[i]==actual_label[i] :
		count=count+1
	else :
		0
print("Accuracy of the test data set is = ",(count/1796)*100)
