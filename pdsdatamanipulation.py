import pandas as pd

"""
'''
data = {
        'name':['raju','siva','anu'],
        'salary':[1000,3000,5000],
    }


df = pd.DataFrame(data,index=['day1','day2','day3'])
print(df)

'''


data = pd.read_csv("D:\\Vcube\\employeedata.csv")


#print(data)

data['Salary'] = data['Salary'].fillna(data.groupby('Department')['Salary'].transform('mean'))

                                                                  

#print('  =========')
    









#data['Salary'] = data['Salary'].fillna(data.groupby('Department')['Salary'].transform('mean'),inplace = True)


#print(data)

res = data.groupby('Department')['Salary'].sum()

res = data.groupby('Department')['Salary'].agg(['sum','max','min','count'])

data['bonus'] = data['Salary']*0.1

data['total'] = data['Salary']+data['bonus']

#data.dropna(inplace=True)
#data.fillna(data.ffill(),inplace=True)

#print(data)

res = data.groupby('Department')['Salary'].sum()

res = data.groupby('Department')['total'].sum()


#print(res.iloc[0:2,0:3]

#data['rank'] = data.groupby('Department')['Salary'].rank(method = 'dense',ascending=False)

#res = data[data['rank'] == 2]

res = data.groupby('Department')['total'].agg(['sum','max','min','count'])


print(data)

data.drop_duplicates(inplace=True)


res = data.groupby('Department')['Name'].count()
'''
for s in data['Salary']:
    if s<30000:
        data['grade'] = 'Low'
    elif s>30000 and s<70000:
        data['grade'] = 'Medium'
    else:
        data['grade'] = 'High'

'''       


res = data['Salary'].max()

#print(data)
#print(data)


print('----')
print()
print(res)

#print(data)


"""


d1 = {
        'name':['siva','anu','raju'],
        'salary':[1000,30000,40000],
        'dept':['dev','test','dev']
    }

d2 = {
        'dept':['dev','test'],
        'loc':['hyd','mumbai']

    }


df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

df = pd.merge(df1,df2,on='dept',how='inner')  # how = 'inner'

print(df)

res = df.loc[0,['name','salary']]

res = df.loc[0:2,['name','dept']]


res = df.iloc[0:2,0:3]



print(df)

print('---- ')
print(res)

'''

def add(a = 2,b = 5):
    return a+b

print(add(None,10))
print(add(undifined,10))

'''
