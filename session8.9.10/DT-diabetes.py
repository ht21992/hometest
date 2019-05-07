import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
from sklearn import tree
col_names=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima=pd.read_csv('diabetes.csv',header=None,skiprows=1,names=col_names)
pima = pima.astype(float)
feature_cols=['pregnant','insulin','bmi','age','glucose','bp','pedigree']
x=pima[feature_cols]
y=pima.label
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
dt=DecisionTreeClassifier(criterion='entropy',max_depth=3,splitter='random')
dt.fit(x_train,y_train)
predicted=dt.predict(x_test)
print(accuracy_score(y_test,predicted))
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
dot_data=StringIO()
export_graphviz(dt,out_file=dot_data,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,class_names=['0','1'])
