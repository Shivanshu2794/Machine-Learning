# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:36:38 2020

@author: Shivanshu
"""

import numpy as np
import sys
import time

s=range(1000) #list

n=np.arange(1000) #np array

print(sys.getsizeof(5)*len(s)) # occupies more space

print(n.size*n.itemsize) #  less space

size=1000000

l1=range(size)
l2=range(size)

n1=np.arange(size)
n2=np.arange(size)

start=time.time()

result=[(x,y) for x,y in zip(l1,l2)]

print((time.time()-start)*1000) #total time taken for list addition in ms

start=time.time()

result=n1+n2 #convenient to add

print((time.time()-start)*1000) #numpy array takes less time for addition 



