# -*- coding: utf-8 -*-
"""
Created on Fri May  )1 19:57:50 2020

@author: Shivanshu Agnihotri
"""


import numpy as np

a=np.array([(1,2,'xyz'),(3,4,5)])

print(a.ndim) #dimesnison of the array
print(a.itemsize) #size of each item
print(a.dtype) #type of items stord
print(a.size) # no of elements
print(a.shape) # no of rows and column 
# print(a.reshape(3,2)) #reshaping the array 

print(a[0:,2]) #slice operation

a=np.array([(1,2,11),(3,4,5)])

# finding min max sum 

print(a.max(),a.min(),a.sum())

#axis sum 

print(a.sum(axis=1))

# add, sub etc can be done directly using operators +,-,/ etc.

print(a.ravel()) #to convert to a single column 




