
#To predict the strongest 11 players taking part in FIFA WC


import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns
import numpy as np 
%matplotlib inline


df=pd.read_csv("FullData.csv")

plt.figure(figsize=(15,32))

plt.figure(figsize=(15,32))
sns.countplot(y=df.Nationality,palette="Set2") #count of players according to their nationality


#delete unnecessary columns
del df['National_Kit']
del df['Nationality']

print(df.head(5))




#code isn't complete yet ........... 


