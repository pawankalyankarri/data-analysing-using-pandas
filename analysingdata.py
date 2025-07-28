import pandas as pd


data = {
        'name':['raju','siva','anu','karthik'],
        'salary':[150000,20000,400000,500000]
    }


df = pd.DataFrame(data,index = [i for i in range(1,len(data['name'])+1)])

#df = pd.DataFrame(data,index = range(1,len(df)+1))
#print(len(df))
#print(df)



#res = [ i for i in range(1,len(data['name']))]

#print(len(data['name']))
#print(res)



df['maxsalary'] = df['salary'].apply(lambda x: 'max' if x == df['salary'].max() else '')
#print(df)


df = pd.read_csv("D:\Vcube\data2.csv")


df['maxCalories'] = df['Calories'].apply(lambda x: 'max' if x == df['Calories'].max() else '')




print(df.to_string())            
