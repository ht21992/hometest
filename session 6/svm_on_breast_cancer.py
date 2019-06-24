import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
BC=pd.read_csv('breast_cancer_dataset.csv')
#print(BC.head)
"""x=BC.drop('class',axis=1)
y=BC['class']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30)
from sklearn.svm import SVC
svclassifier=SVC(kernel='linear')
svclassifier.fit(x_train,y_train)
y_pred=svclassifier.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix
#print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))"""
"""x=BC.drop('class',axis=1)
y=BC["class"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
from sklearn.svm import SVC
svclassifier=SVC()
#by default kernel is rbf
svclassifier.fit(x_train,y_train)
y_predict=svclassifier.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,y_predict))"""
x=BC.drop('class',axis=1)
y=BC['class']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)
from sklearn.svm import SVC
svclassifier=SVC(kernel='sigmoid')
svclassifier.fit(x_train,y_train)
y_predict=svclassifier.predict(x_test)
from sklearn.metrics import confusion_matrix,classification_report
print(classification_report(y_test,y_predict))
"""fig=plt.figure()
ax=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax.plot(x)
ax2.plot(y)
plt.show()"""