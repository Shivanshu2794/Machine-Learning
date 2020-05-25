import pandas as pd
import numpy as np

from numpy.random import randn

df = pd.DataFrame({'Name': ['A', 'B', 'C'],
                        'Val': [10, 10, 20]},
                        index=[0, 1, 2])
df['Val'].unique() # unique values 
df['Val'].nunique() # no of unique values

df['Val'].value_counts()

def square(x):
    return x**2
    

df['Val'].apply(square) # applying functions

df['Val'].apply(lambda x: x +10)

df.columns

df.drop('Val',axis=1)  #dropping column

# use del to permanently delete del df['Val']






