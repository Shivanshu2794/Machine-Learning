import pandas as pd
import numpy as np

from numpy.random import randn

df1 = pd.DataFrame({'IND': ['A', 'B', 'C'],
                        'RUS': ['D', 'E', 'F']},
                        index=[0, 1, 2])

df2 = pd.DataFrame({'ENG': ['X', 'Y', 'Z'],
                        'USA': ['W', 'X', 'Y']},
                        index=[4, 5, 6]) 

df1
df2
pd.concat([df1,df2]) #concatenating data frames

# merging 

left = pd.DataFrame({'key': [1, 2, 3],
                     'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']})
   
right = pd.DataFrame({'key': [1, 2, 3],
                          'C': ['C0', 'C1', 'C2'],
                          'D': ['D0', 'D1', 'D2']})  

pd.merge(left,right,how='inner',on='key')

# joining 

left = pd.DataFrame({
                     'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},index=(0,1,2))
   
right = pd.DataFrame({
                          'C': ['C0', 'C1', 'C2'],
                          'D': ['D0', 'D1', 'D2']},index=(1,2,3))  

left.join(right,how="outer")

