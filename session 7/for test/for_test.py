import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
data1=pd.read_csv("live_table.csv")
data2=pd.read_csv("calendar.csv")
data1=data1.drop(["+/-","Pts"],axis=1)
data2=data2.drop(["ID","Date","Time","Status","H HT Score","A HT Score","Attendance"],axis=1)
#print(data1.head())
#print(data2.head())
data2=data2[0:40]
X=data2.drop(["H Score","A Score"],axis=1)
ind=[0 for i in range(20)]
#datan={'H Score':list(data2["H Score"])}
Y=data2["H Score"]
labelEncoder=LabelEncoder()
labelEncoder.fit(X['Home Team'])
labelEncoder.fit(X['Away Team'])
X['Home Team']=labelEncoder.transform(X['Home Team'])
X['Away Team']=labelEncoder.transform(X['Away Team'])
x_train,x_test,y_train,y_test=train_test_split(X,Y)
svclassifier=SVC(kernel='linear')
svclassifier.fit(x_train,y_train)
ypredict=svclassifier.predict(x_test)
"""plt.plot(y_train)
plt.plot(ypredict)
plt.show()"""
print(list(y_test))
print(list(ypredict))
from sklearn.metrics import classification_report,confusion_matrix
#print(confusion_matrix(y_test,ypredict))
print(classification_report(y_test,ypredict))
