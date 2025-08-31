

with open("C:\\Users\\pawan\\Python\\sample.txt",'a+') as file:
    file.write('\nhere iam adding extra line ')
    file.write('\nit is another line')
    file.seek(0)
    data = file.read()

#print(data)



with open("C:\\Users\\pawan\\Python\\sample.txt",'w+') as file:
    file.write("What does the with statement do in file handling?\nIt automatically closes the file after the block is done. It's cleaner and safer\n")
    file.seek(0)
    data = file.read()

#print(data)


import csv
arr = []

with open("D:\\Vcube\\emp.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    arr.append(header)
    #print(header)
    for row in reader:
        arr.append(row)
        #print(row)


#print(arr)

import numpy as np

res = np.array(arr)

#print(res)




import os

res = os.path.isfile("D:\\Vcube\\emp.csv")
#print(res)


with open("D:\\Vcube\\sample3.txt",'w+') as file:
    file.write('\n This is first line')
    file.write('\n this is second line')
    file.seek(0)
    data = file.read()

#print(data)


with open("D:\\Vcube\\csv1.csv",'w+',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','salary'])
    writer.writerow(['raju',10000])
    file.seek(0)
    reader = csv.reader(file)
    for i in reader:
        print(i)
        
    















    
'''

if os.path.isfile("D:\\Vcube\\csv1.csv"):
    print('yes')
    #os.remove("D:\\Vcube\\csf1.csv")
    

with open("D:\\Vcube\\csv1.csv",'w+',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','salary'])
    writer.writerow(['raju',10000])
    file.seek(0)
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
'''    
