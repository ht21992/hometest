from sklearn import datasets
iris=datasets.load_iris()
#print(iris.feature_names)
#print(iris.target_names)
#print(iris[0:6])
#print(iris.target)
import pandas as pd
data=pd.DataFrame({'sepal length':iris.data[:,0],'sepal width':iris.data[:,1],'petal length':iris.data[:,2],'petal width':iris.data[:,3],'species':iris.target})
from sklearn.model_selection import train_test_split
x=data[['sepal length','sepal width','petal length','petal width']]
y=data['species']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
from sklearn.ensemble import RandomForestClassifier
RFC=RandomForestClassifier(n_estimators=100)
RFC.fit(x_train,y_train)
predicted=RFC.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predicted))
feature_imp=pd.Series(RFC.feature_importances_,index=iris.feature_names).sort_values(ascending=False)
#print(feature_imp)