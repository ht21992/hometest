import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score

#load the diabetes dataset
diabetes=datasets.load_diabetes()
#use only one feature
diabetes_X=diabetes.data[:,np.newaxis,2]
#split the data into training/testing sets
diabetes_X_Train=diabetes_X[:-20]
diabetes_X_Test=diabetes_X[-20:]
#split the target into training/testing sets
diabetes_Y_Train=diabetes.target[:-20]
diabetes_Y_Test=diabetes.target[-20:]
#create linear regression object
regr=linear_model.LinearRegression()
#Train the model using the training sets
regr.fit(diabetes_X_Train,diabetes_Y_Train)
#Make predictions using the testing set
diabetes_y_predictions=regr.predict(diabetes_X_Test)
plt.scatter(diabetes_X_Test,diabetes_Y_Test,color="black")
plt.scatter(diabetes_X_Test,diabetes_y_predictions,color="blue",linewidths=3)
plt.xticks(())
plt.yticks(())
plt.show()