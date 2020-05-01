# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:19:40 2020

@author: Shivanshu Agnihotri
"""

import numpy as np 

import matplotlib.pyplot as plt

x= np. arange (0,3*np.pi,0.1) 

y=np.cos(x) #grpah

plt.plot(x,y)

plt.show()

n=np.array([1,2,3])

print(np.exp(n)) #exponantial of array elements 

print(np.log10(n)) # log base 10 

print(np.log(n)) # natural log

