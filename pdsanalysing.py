import pandas as pd

#pd.options.display.max_rows = 100

data = pd.read_csv("D:\\Vcube\\data2.csv")



#print(data)


data = pd.read_csv("D:\\Vcube\\employeedata.csv")

#print(data)


res = data.groupby('Department')['Salary'].sum()

data['bonus'] = data['Salary'].apply(lambda x: x*0.1)

#data.fillna(data.ffill(),inplace = True)


#data.fillna(data.bfill(),inplace = True)

#data.dropna(inplace = True)


data.fillna(data.ffill(),inplace = True)


#res = data['Salary'].max()

res = data['Salary'].min()

print(data)

res = data.groupby('Department')['Department'].count()

res = data.groupby('Department')[['Salary','bonus']].sum()



res = data.groupby('Department')['Salary'].agg(['sum','max','min','count'])

res = data.groupby('Department')['Salary'].sum()

res = data.groupby('Department')['bonus'].max()

res = data.groupby('Department')['Salary'].min()



res = data.groupby('Department')['bonus'].max()

res = data.groupby('Department').count()

res = data.groupby('Department')['Salary'].min()

res = data.groupby('Department')[['Salary','bonus']].mean()

res = data.groupby('Department')[['Salary','bonus']].max()

data['total'] = data['Salary']+data['bonus']

res = data.groupby('Department')['total'].max()

res = data.groupby('Department')['bonus'].agg(['count','sum'])


#res = data.groupby('Department')['Salary'].mean()


#res = res[res>50000]


#max_sal = data.groupby('Department')['Salary'].transform('max')

#res = data[data['Salary'] == max_sal]


max_sal = data.groupby('Department')['Salary'].transform('max')

print(max_sal)

res = data[data['Salary'] == max_sal]

max_sal = data.groupby('Department')['Salary'].transform('max')

res = data.groupby('Department')['Salary'].max() # it will give department and max salary

max_sal = data.groupby('Department')['Salary'].transform('max')

res = data[data['Salary'] == max_sal]




print(data)

res = data.groupby('Department')['total'].sum()

res = res.sort_values(ascending=False)




print('--------')
print(res)


#print(res)

#print(data)

#print(data.to_string())











































