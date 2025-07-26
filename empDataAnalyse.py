import pandas as p

data = {'name':['siva','raju','anu','hari','rajesh','sravya','karthik'],
        'salary':[15000,20000,250000,300000,50000,350000,360000],
        'dept':['dev','test','management','dev','test','dev','management'],
        }


df = p.DataFrame(data)
res = df.sort_values(by='salary',ascending=False)

res = df[['name','salary']]

res = df['salary'].describe()

res = df['salary'].sum()

df.dropna(inplace=True)

df.fillna(df.ffill(),inplace=True)

df.fillna(df.bfill(),inplace=True)


df.fillna(df.ffill(),inplace=True)


res = df.head()

res = df.tail()

res = df[df['salary']>50000]

res = df[df['name'].str.contains('u')]

res = df[df['name'].str.contains('r')]

res = df.sort_values(by='salary',ascending=True)

res = df[df['salary']>50000]

res = df[df['name'].str.contains('s')]

res = df.groupby('dept')['salary'].sum()

res = df.groupby('dept')['name'].count()

res = df.loc[0:2,['name','salary']]

res = df.loc[0,['name','salary']]

res = df.loc[0:5,['name','salary']]

res = df.iloc[0:2,0:2]












print(res)
print(df)



data1 = {
    'name':['siva','raju','anu','rajesh','surya','abinav'],
    'salary':[50000,30000,600000,700000,360000,2600000],
    'dept':['dev','test','dev','test','dev','test']

    }


data2 = {
        'dept':['dev','test'],
        'loc':['hyd','mumbai']
    }


df1 = p.DataFrame(data1)
df2 = p.DataFrame(data2)

df = p.merge(df1,df2,on='dept')


print(df)





















