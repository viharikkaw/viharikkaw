#pip install seaborn
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
data={'name':["a","b","c","d","e"],'age':[24,35,45,25,44],'dept':["CSE","CS","IOT","DSA","AIML"],'salary':[21000,25000,55000,64000,36000],'joindate':pd.to_datetime(['2022-06-01','2021-08-05','2023-12-23','2021-11-22','2022-10-23'])}
df=pd.DataFrame(data)
labels=df['name'].tolist()
ages=df['age'].tolist()
plt.bar(labels,ages,color="red")
plt.show()
