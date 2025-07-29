import pandas as pd

data = pd.read_csv("D:\\Vcube\\emp.csv")
#print(data)

res  = data.groupby('Department')['Salary'].sum()

res = data.groupby('Department')['Salary'].count()

#data.drop_duplicates(inplace=True)

res = data.groupby('Department')['Salary'].mean()

res = data.groupby('Department')['Salary'].max()

data.loc[1,'Salary'] = 850000



#print(data)

#data['Max_sal'] = data['Salary'].apply(lambda x: 'max if x == data['Salary'].max() else '')





print(data)

#data['Max_sal'] = ''

lst = data.groupby('Department')['Salary'].max().to_dict()


print(lst)

data['Max_sal']  = ' '

'''
for i in data:

    if i == 'Salary':
        if data['Salary'] == data.groupby('Department').max():
            data['Max_sal'] = 'max'

print(data)

'''

#print(lst['HR'])

for row,col in data.iterrows():
    sal = col['Salary']
    dept = col['Department']
    mx = col['Max_sal']
    
    if lst[dept] == sal:
        print(row)
        data.loc[row,'Max_sal'] = 'max'
       

print(data)

     
    



#print(data)

print()
#print(res)
