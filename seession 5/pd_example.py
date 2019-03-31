import pandas as pd
data={"Name":["Andrew","Rob","Marry"],"LastName":["Martinz","Jhonson","Patrics"],"Age":[26,28,28]}
indexs=["Person1","Person2","Person3"]
df=pd.DataFrame(data,index=indexs)
#print(df)
#print(df.loc["Person1"])
#print(df["Age"])
#print(df.iloc[0,2])
#print(df.sum())
#print(df.mean())
#import  matplotlib.pyplot as plt
#df.plot.bar()
#plt.show()
#df.to_csv("example.csv")
#df=pd.read_csv('example.csv',index_col=0)