import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101) # same random numbers

df = pd.DataFrame(randn(3,2),['A','B','C'],['X','Y'])

print(df,'\n',df['X'])  #selection
type(df['X']) #bunch of series

df[['X','Y']] #column selection

df['new'] = df['X'] + df['Y']
df
df.drop('new',axis=1)

df.shape
df

df.loc['A'] #row selection
df.iloc[2] # row selection based on index
df.loc['A','X'] # subset selection

# conditional selection

df > 0
new = df > 0
df[new] 


df[df['X']>0] # selecting only those dataframe where X has values greater thant 0 
df[df['Y']<0]

df[(df['X']>0) & (df['Y']>1)]

df.reset_index()

new="INDIA USA CHINA".split()
df['country']=new
print(df)

# index levels

out=['X','X','Y','Y']
ins=[1,2,1,2]
index=list(zip(out,ins))
index

index=pd.MultiIndex.from_tuples(index)
index
df=pd.DataFrame(randn(4,2),index,['A','B']) #multilevel indexing
df
df.loc['X']
df.index.names=['Grp','Prob'] #naming indices
df
df.loc['Y'].loc[2]['B'] #particular accessing

#cross section
df.xs(1,level='Prob')




