print(" Hello this my first ML project")
import numpy as np
import pandas as pd
iris = pd.read_csv('iris.csv')

print(iris.shape)
iris.describe()

x=iris.drop(columns=['class'])

y=iris['class']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.4)
print(x_train)
print(y_train)
print(x_test)
print(y_test)
from sklearn import neighbors
classifier1=neighbors.KNeighborsClassifier()

classifier1.fit(x_train,y_train)

predictions=classifier1.predict(x_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, predictions))

from sklearn import tree
classifier2=tree.DecisionTreeClassifier()

classifier2.fit(x_train,y_train)
predictions=classifier2.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))