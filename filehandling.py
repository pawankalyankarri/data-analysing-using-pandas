with open("C:\\Users\\pawan\\Python\\sample.txt",'r') as file:
    data = file.read()

#print(data)


#with open("C:\\Users\\pawan\\Python\\sample.txt", 'a') as file:
#  file.apend('\\n here i am modified')

'''
with open("C:\\Users\\pawan\\Python\\sample.txt",'r') as file:
    data = file.readlines()


for i in data:
    print(i,end=' ')

    
'''

with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    l1 = file.readline()
    l2 = file.readline()
    l3 = file.readline()


#print(l1)
#print(l2)
#print(l3)

import pandas as pd

data = {
        'name':['siva','anu','raju'],
        'salary':[1000,30000,50000],

    }

df = pd.DataFrame(data)

#print(df)

df.to_csv('res.csv',index = False)

res = pd.read_csv('res.csv')
#print(res)


with open('C:\\Users\\pawan\\Python\\sample.txt','w') as file:
    file.write('Here i am overiting ')

with open('C:\\Users\\pawan\\Python\\sample.txt','r') as file:
    data = file.read()

#print(data)
'''
with open('C:\\Users\\pawan\\Python\\sample.txt','w+') as file:
    file.write('third ovverrite')
    file.seek(0)
    data = file.read()

#print(data)
'''

with open('C:\\Users\\pawan\\Python\\sample.txt','a+') as file:
    file.write('\ni am appending here\n')
    file.seek(0)
    data = file.read()

#print(data)


import os

if os.path.exists('sample.txt'):
    print('file is exists')
else:
    #print('file not exists')
    pass


with open('C:\\Users\\pawan\\Python\\sample.txt') as file:
    lines = file.readlines()

for i in lines:
    print(i)
 