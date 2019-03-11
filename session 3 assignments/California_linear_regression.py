from sklearn.datasets.california_housing import fetch_california_housing
data=fetch_california_housing()
from sklearn.model_selection._split import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data.data,data.target)
from sklearn.linear_model import LinearRegression
clf=LinearRegression()
clf.fit(x_train,y_train)
prdicted=clf.predict(x_test)
expected=y_test
import matplotlib.pyplot as plt
plt.figure(figsize=(4,3))
plt.scatter(expected,prdicted)
plt.plot([0,50],[0,50],"--k")
plt.axis("tight")
plt.xlabel("True price ($1000s)")
plt.ylabel("Predicted price ($1000s)")
plt.tight_layout()
plt.show()