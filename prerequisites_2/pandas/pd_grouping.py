import pandas as pd
import numpy as np

from numpy.random import randn


data = {'Country':['IND','IND','IND','AUS','AUS'],'Cricketer':['Virat','Dhoni','Rohit','Ponting','Gilly'],'Scores':[200,180,340,170,180]}
df=pd.DataFrame(data)
df

#grouping by columns
a=df.groupby('Country')
a.mean()
a.sum().loc['IND'] # summing scores of cricketers from india

a.describe() # performs some aggregate operations on data 

