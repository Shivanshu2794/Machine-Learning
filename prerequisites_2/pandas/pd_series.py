import numpy as np
import pandas as pd

new=['x','y','z']
data=[4,5,6]
arr=np.array(data)
d={'x':4,'y':5,'z':6}
print(arr,d)

#Series
pd.Series(data=data)
pd.Series(data=data,index=new)
pd.Series(data,new)

# can hold any type of data
pd.Series(data=new)

#index
s1=pd.Series([1,2,3],['X','Y','Z'])
s1['X']
s2=pd.Series([10,2,30],['X','Y','V'])

#operation
s1+s2


