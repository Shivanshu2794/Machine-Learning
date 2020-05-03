"""
Created on Fri May  2 13:41:40 2020

@author: Shivanshu Agnihotri
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

a=sns.load_dataset("iris")
b=sns.FacetGrid(a,col="species")
b.map(plt.hist,"sepal_length")
