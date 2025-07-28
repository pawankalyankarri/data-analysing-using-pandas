#find the longest string

with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
        data = file.read()

#print(data)

res =  ''

for i in data.split():
    if len(i)>len(res):
        res = i

#print(res)

with open("C:\\Users\\pawan\\Python\\sample2.txt",'a+') as file:
    #print(file)
    for i in file:
        #print(i)
        pass
    file.write(data)
    file.seek(0)
    data1 = file.read()

#print(data1)


with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()
    
print(data)
word = 'java'
what = 'easy'
res = ''
for i in range(len(data)):
    if data[i:i+len(what)] == what:
        res = data[:i]+word+data[i+len(what):]
print('----')
print(res)
        
    
