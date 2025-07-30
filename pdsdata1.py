import pandas as pd
'''
data = {
        'name':['siva','raju','anu','sravya'],
        'salary':[15000,2000,50000,30000],
        'dept' :['dev','test','dev','manag']
    }


df = pd.DataFrame(data)
print(df)

#df['max'] = df['salary'].apply(lambda x: 'max' if x == df['salary'].max() else ' ' )


res = df.groupby('dept')['salary'].sum().to_dict()



print(res)

df['maxsal'] = ' '

for row,col in df.iterrows():
    print(row,col)

#for row,col in df.iter

#print(df)


'''


data = pd.read_csv("D:\\Vcube\\data3.csv")

print(data)

#res = data.isnull().sum()

data.drop_duplicates()

res = data.groupby('Gender').count()

res = data.groupby('Department')['Salary'].sum().to_dict()

res = data.groupby('Department')['Salary'].mean()

res = data[data['Salary']>60000]

res = data['Department'].nunique()

res = data.sort_values(by='Salary',ascending=False)

res = data[data['Joining_Date'] > '2020-12-31']

data['experience'] = pd.to_datetime('2025-01-01')-pd.to_datetime(data['Joining_Date'])


                       

print('==========>>>')
#print(res)

print(data)
















import numpy as np

#res = np.array([[i for i in range(1,11) if i%2 == 0],[i for i in range(1,11) if i%2 == 1]])

#res = np.array([1,2,3,4,5],ndmin=64)

#print(res)
