import pandas as pd
import numpy as np

from numpy.random import randn

d={'X':[1,2,3],'Y':[3,np.nan,4],'C':[5,np.nan,np.nan]}

df=pd.DataFrame(d)
df
# dropping rows and column containing NaN

df.dropna()
df.dropna(axis=1) 

df.dropna(thresh=2) # dropping rows having atleast 2 NaN

df.fillna(value='FILL') # filling missing values

df['Y'].fillna(value=df['X'].mean(),inplace=True) # filling with mean 
df
