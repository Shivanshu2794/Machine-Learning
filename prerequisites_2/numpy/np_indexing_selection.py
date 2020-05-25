# array indexing and selection

import numpy as np

arr=np.arange(0,11)
arr
arr[1:5]

arr[0:2]=100 #broadcasting
print(arr)

arr=np.arange(0,15)

s=arr[0:7]
s
s[:] = 50
print(s,arr) #changed in original array (doesnt not copy)
copy=arr.copy() # to explicit copy 
print(copy)

# 2d arrays

x=np.array([[0,1,2],[3,4,5]])
print(x,'Acccessing ->',x[0][2])

# single and double bracket access

print(x[1,2],' is same as ',x[1][2])

# accessing part of matrix
print(x[:2,1:])
print(x[1:,1:])


arr=np.arange(0,10)
barr=arr>4

# effective selection 
print(barr)  
print(arr[arr>3])

xyz=np.arange(100).reshape(10,10)
print(xyz,'\n',xyz[1:3,4:])

ss
