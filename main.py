import pandas as pd
import numpy as np
#read file
df=pd.read_csv('company_employees_dataset.csv')

#checking starting 5 rows
print(df.head())

#checking size
print(df.shape)

#checking null values in coloums #any-- just tell true or false not count
print(df.isnull().sum())

#checking data types and null values count
print(df.info())

#checking statistical info
print(df.describe())

#filling null values by using mean
df['Salary']=df['Salary'].fillna(df['Salary'].mean())

#checking is there still null values or not
print(df['Salary'].isnull().sum())

#still 23 null values remaining in PerformanceScore
df['PerformanceScore']=df['PerformanceScore'].fillna(df['PerformanceScore'].mean())

#checking is there still null values or not
print(df['PerformanceScore'].isnull().sum())

#Incorrect Gender Values correction
df['Gender']=df['Gender'].replace({
    'M' : 'Male',
    'Fmale' : 'Female'
    })
print(df['Gender'].unique())

#checking how many duplicated rows we have
print(df.duplicated().sum())

#checking which rows are duplicated
print(df[df.duplicated()])

#dropping duplicates
df.drop_duplicates(inplace=True)

#now again checking if there are duplicates or not
print(df.duplicated().sum())

#checking how many unique ids we have with nunique
print(df['EmployeeID'].nunique())

#department vise employee count
print(df['Department'].value_counts())

#department vise average salary checking
print(df.groupby('Department')['Salary'].mean().round(0).astype(int))

#Gender Distiribution count
print(df['Gender'].value_counts())

#Department vise Gender Distribution count
print(df.groupby('Department')['Gender'].value_counts())

#Employees Status Check
print(df['Status'].value_counts())

#Checking highest Salary by sorting in descending order
df=df.sort_values('Salary',ascending=False)
print(df[['EmployeeID','Name','Salary']].head())

#department vise performancescore average
print(df.groupby('Department')['PerformanceScore'].mean())

#Convert JoinDate into proper formate
df['JoinDate']=pd.to_datetime(df['JoinDate'])
#Extract year from joindate
df['Year']=df['JoinDate'].dt.year
#show year starting 5 rows
print(df['Year'].head())

#year vise employee count check kya
print(df.groupby('Year')['EmployeeID'].count())

#correlations check krrahe
print(df[['Age','Salary','PerformanceScore']].corr().round(2))

#Clean Dataset save
df.to_csv('New Employees.csv', index=False)

df_new = pd.read_csv('New Employees.csv')
print(df_new.head())
print(df_new.shape)
print(df_new.columns)