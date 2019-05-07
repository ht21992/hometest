weather=['Sunny','Sunny','Overcast','Rainy','Sunny','Overcast','Rainy','Sunny','Overcast','Rainy','Sunny','Sunny','Overcast','Rainy']
temp=['Hot','Hot','Mild','Cool','Hot','Hot','Mild','Cool','Hot','Hot','Mild','Cool','Mild','Cool']
play=['No','No','Yes','Yes','No','No','Yes','No','No','Yes','Yes','No','Yes','Yes']
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
weather_encoded=le.fit_transform(weather)
temp_encoded=le.fit_transform(temp)
play_label=le.fit_transform(play)
features=list(zip(weather_encoded,temp_encoded))
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(features,play_label)
pridcted=model.predict([[0,2]])
print(pridcted)