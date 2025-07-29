import pandas as pd

data = pd.read_excel("D:\\Vcube\\slots.xlsx")
#print(data)

data = {
        'name':['raju','siva','anu'],
        'salary':[10000,30000,50000]
    }

df = pd.DataFrame(data)
print(df)
print('------>')

#print(df.shape[0])

lst = df.columns.tolist()
#print(lst)

#print(df.index)

#print(df.dtypes)

#print(df.info())

#print(df.describe)

#print(df.head())
#print(df.tail())

#df['rank'] = df['salary'].rank(method = 'dense',ascending=False)


#print(df['name'])
#print(df['salary'])

#print(df.loc[5])

#print(df.loc[0,['name','salary']])


res = df[df['salary']>30000]


df.replace('raju','rajesh',inplace = True)

df.duplicated()

lst = [('aravind',50000),('suri',55000)]

for i in lst:
    df.loc[len(df)] = i


#df.drop_duplicates(inplace=True)



#df.rename(columns={'name':'Name'},inplace = True)

df['name'] = df['name'].apply(lambda x:x.upper())



#df.loc[0,'salary'] = None

#res = df.isnull()


df.sort_values('salary',ascending=False,inplace = True)

#df.rename(columns={'name':'Name'},inplace = True)


#df['cumsum'] = df['salary'].cumsum()

#df['new'] = df['salary'].rolling(window=3).sum()


res = df.value_counts()


    
print(res)

print(df)





