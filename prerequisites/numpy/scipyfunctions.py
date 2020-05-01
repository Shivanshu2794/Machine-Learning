# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:35:19 2020

@author: Shivanshu
"""


from scipy import special
from scipy import integrate
import numpy as np 
from scipy import linalg


n=special.exp10(2) #exponantial

x=special.sindg(90) # value of sin angle 
print(n,x) 

i=integrate.quad(lambda x: special.exp10(2),0,1) #integration 
print(i)

a=np.array([[1,2],[3,4]])
b=linalg.inv(a)
print(b) # inverse of matrix (linear algebra)

