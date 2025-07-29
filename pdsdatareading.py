with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()
    for i in file:
        #print(i)
        pass

#print(data)

#cnt = data.count('\n')+1

cnt = 0

for i in data:
    if i == '\n':
        cnt+=1

else:
    cnt+=1


#print(cnt)



#"D:\\Vcube\\employeedata.csv"

import csv

with open("D:\\Vcube\\employeedata.csv") as file:
    reader = csv.reader(file)
    header = next(reader)

    idx = header.index('EmployeeID')
    nameidx = header.index('Name')
    deptidx = header.index('Department')



#print(idx)
#print(nameidx)
#print(deptidx)
#print(header)




data = {
        'x':[1,2,3,4,5,6],
        'y':[9,8,7,6,5,4],
    }

import pandas as pd
import matplotlib.pyplot as pt

df = pd.DataFrame(data)
df.plot(x='x',y='y')
#pt.show()



with open("C:\\Users\\pawan\\Python\\sample.txt",'w+') as file:
    file.write('here i am overwrited')
    file.seek(0)
    data = file.read()

print(data)

