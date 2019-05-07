from sklearn import datasets
wine=datasets.load_wine()
#print(wine.feature_names)
#print(wine.target_names)
#print(wine.data.shape)
#print(wine.data[0:7])
#print(wine.target)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.3,random_state=109)
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(x_train,y_train)
predicted=gnb.predict(x_test)
from sklearn import metrics
#print(classification_report(y_test,predicted))
print(metrics.accuracy_score(y_test,predicted))
