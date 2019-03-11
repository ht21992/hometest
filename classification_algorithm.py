
from sklearn import tree
x="ab"
y=[]
z=''
for char in x:
   y.append(ord(char))
for digit in y:
   z+=chr(digit)


fruits=[["yellow","long"],["green","long"],["orange","round"]]
label=["banana","cucumber","orange"]
test_data=[["orange","round"]]
x1=[]
y1=[]
for fruit in fruits:
   for word in fruit:
     for char in word:
         x1.append(ord(char))
print(x1)
for fruit in label:
    for char in fruit:
        y1.append(ord(char))
print(y1)
#dtc_clf=tree.DecisionTreeClassifier()
#dtc_clf=dtc_clf.fit(x1,y1)