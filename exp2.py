#pandas
import pandas as pd
import datetime as dt
data={'name':["a","b","c","d","e"],'age':[24,35,45,65,44],'dept':["CSE","CS","IOT","DSA","AIML"],'salary':[21000,25000,55000,64000,36000],'joindate':pd.to_datetime(['2022-06-01','2021-08-05','2023-12-23','2021-11-22','2022-10-23'])}
print(data)
df=pd.DataFrame(data)
#print(df)
print(df.head(3)) 
print(df.shape)
print(df.dtypes)
arr=df.columns.tolist()
print(arr)

#filtering
#col based filtering
#print(df[['name','dept']])
#print(df[df['dept']=='IT'])
#print(df[df['salary']>15000])
#print(df[(df['dept']=="CSE") & (df['salary']>25000)])
#print(df)
#print(df['salary'].max())
#print(df.groupby('dept')['salary'].sum())
#print(df['dept'].value_counts())
df['bonus']=df['salary']*0.10 
#print(df)
#import datetime as dt
df['joiningyear']=df['joindate'].dt.year
#print(df)
df.rename(columns={'joindate':'joiningdate'},inplace=True)
#print(df)
#df.drop(columns=['joiningyear'],inplace=True)
#print(df)
#df=df.sort_values(by='salary',ascending=False)
#print(df)
#print(df.loc[df.groupby('dept')['salary'].idxmax()])
#print(df)
#seniority based on age
df['seniority']=df['age'].apply(lambda x: 'senior' if x>30 else 'junior')
print(df)
df.to_csv("employee.csv",index=False)