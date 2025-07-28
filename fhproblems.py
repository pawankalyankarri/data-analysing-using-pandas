with open("C:\\Users\\pawan\\Python\\sample.txt",'r') as file:
    data  = file.read()

cnt = 0
#print(data)

'''
delimiter = [' ',',','|']
k = 0
for i in range(len(data)):
    if data[i] in delimiter:
        cnt+=1

else:
    cnt+=1
        

print(cnt)
'''

with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()

delimeter = [' ',',','|']
cnt = 0
p = 0
res = []
for i in range(len(data)):
    if data[i] in delimeter:
        res.append(data[p:i])
        cnt+=1
        p = i
else:
    res.append(data[p:])
    cnt+=1

#print(cnt)
#print(res)


'''
with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()

d = {}
for ch in data:
    ch = ch.lower()
    d[ch] = d.get(ch,0)+1

print(data)
print(d)

'''

with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()


delimeter = [' ',',']
p = 0
arr = []
for i in range(len(data)):
    if data[i] in delimeter:
        
        arr.append(data[p:i])
        p = i+1
        

else:
    arr.append(data[p:])
cnt = 0
for i in arr:
    cnt+=1
    
#print(data)
#print(cnt)
    
#print(arr)

lst = ['one','two','three']
'''
for i in lst:
    with open("C:\\Users\\pawan\\Python\\sample.txt",'a') as file:
        file.write(i+'\n')

with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()

print(data)

'''

with open("C:\\Users\\pawan\\Python\\sample.txt",'a+') as file:
    file.write('\n'.join(lst))

with open("C:\\Users\\pawan\\Python\\sample.txt") as file:
    data = file.read()

print(data)








        
