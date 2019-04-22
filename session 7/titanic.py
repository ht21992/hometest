import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
#load train and test datasets to create two DataFrames
train_url="http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train=pd.read_csv(train_url)
test_url= "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test=pd.read_csv(test_url)
#servival count based on different attributes ?????????????
train[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Survived',ascending=False)
train[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by='Survived',ascending=False)
train[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='Survived',ascending=False)
#droping unnecessary columns in train and test
train=train.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
test=test.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
#converting features to numeric(label encoding)
labelEncoder=LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex']=labelEncoder.transform(train['Sex'])
test['Sex']=labelEncoder.transform(test['Sex'])
#Labeling (question)
X=np.array(train.drop(['Survived'],1).astype(float))
Y=np.array(train['Survived'])
print("************Train Set*********")
print(train.head())
print(train.describe())
print("************in the Train Set*********")
#filling missing values with the mean column value in the train set
train.fillna(train.mean(),inplace=True)
print(train.isna().sum())
#some features are not numeric so we need to convert them.by this command we'll find data types
print(train.info())
print("\n")
print("************Test Set*********")
print(test.head())
print(test.describe())
print("************in the Test Set*********")
#filling missing values with the mean column value in the test set
test.fillna(test.mean(),inplace=True)
print(test.isna().sum())

#train the model ????????
kmeans=KMeans(n_clusters=2) # we want to cluster the passenger records into 2 survived or not survived
"""kmeans.fit(X)
#calculating correctness
correct=0
for i in range(len(X)):
    predict_me=np.array(X[i].astype(float))
    predict_me=predict_me.reshape(-1,len(predict_me))
    prediction=kmeans.predict(predict_me)
    if prediction[0]==Y[i]:
        correct+=1
    print(correct/len(X))
#adjusting the K-means params
kmeans=KMeans(n_clusters=2,max_iter=600,algorithm='auto')
kmeans.fit(X)
#kmeans=KMeans(n_clusters=2,max_iter=600,algorithm='auto')
#kmeans.fit(X)"""
"""fig=plt.figure()
ax=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)
ax.plot(train[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Survived',ascending=False))
ax2.plot(train[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='Survived',ascending=False))
ax3.plot(train[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by='Survived',ascending=False))
plt.show()
print("********X*******")
print(X)
print("*********Y**********")
print(Y)
print(train.info())"""
