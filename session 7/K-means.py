import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
""" i tried to used fifa 19 dataset to predict a player is right foot or left foot base on Value and Wage and Nationality(Name is only for my better understanding)"""
fifa19=pd.read_csv("data.csv")
list_to_drop=["Club","Position","ID","Photo","Flag","Club Logo","Special","International Reputation","Work Rate","Weak Foot","Skill Moves"
              ,"Body Type","Real Face","Jersey Number","Joined","Loaned From","Contract Valid Until","Height","Weight",
              "LS","ST","RS","LW","LF","CF","RF","RW","LAM","CAM","RAM","LM","LCM","CM","RCM","RM","LWB","LDM","CDM","RDM",
              "RWB","LB","LCB","CB","RCB","RB","Crossing","Finishing","HeadingAccuracy","ShortPassing","Volleys","Dribbling",
              "Curve","FKAccuracy","LongPassing","BallControl","Acceleration","SprintSpeed","Agility","Reactions","Balance",
              "ShotPower","Jumping","Stamina","Strength","LongShots","Aggression","Interceptions","Positioning","Vision","Penalties","Composure",
              "Marking","StandingTackle","SlidingTackle","GKDiving","GKHandling","GKKicking","GKPositioning","GKReflexes","Release Clause"]
fifa19=fifa19.drop(list_to_drop,axis=1)
fifa19.fillna(fifa19.mean(),inplace=True)
#because there were some null blocks on Preferred Foot columns so i needed to fill them all first with sth then try to use label encoder
fifa19["Preferred Foot"].fillna("Right",inplace=True)
labelEncoder=LabelEncoder()
labelEncoder.fit(fifa19["Name"])
fifa19["Name"]=labelEncoder.transform(fifa19["Name"])
labelEncoder.fit(fifa19["Preferred Foot"])
fifa19["Preferred Foot"]=labelEncoder.transform(fifa19["Preferred Foot"])
labelEncoder.fit(fifa19["Nationality"])
fifa19["Nationality"]=labelEncoder.transform(fifa19["Nationality"])
labelEncoder.fit(fifa19["Wage"])
fifa19["Wage"]=labelEncoder.transform(fifa19["Wage"])
labelEncoder.fit(fifa19["Value"])
fifa19["Value"]=labelEncoder.transform(fifa19["Value"])
#X=fifa19.drop("Preferred Foot",axis=1)
#print(X.isna().sum())
X=np.array(fifa19.drop("Preferred Foot",axis=1).astype(float))
#print(X.isna().sum())
#Y=fifa19["preferred Foot"]
Y=np.array(fifa19["Preferred Foot"])
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)

correct=0
for i in range (len(X)):
    predict_me=np.array(X[i].astype(float))
    predict_me=predict_me.reshape(-1,len(predict_me))
    prediction=kmeans.predict(predict_me)
    if prediction[0]==Y[i]:
        correct+=1
print(correct/len(X))

