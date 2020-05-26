import pandas as pd
import numpy as np

df=pd.read_csv('Ecommerce Purchases')
df.head(5)

df.columns

df['Purchase Price'].mean() 

df[df['Language']=='en'].count() #people having langugae as en

df['AM or PM'].value_counts() # purchase made at AM and PM separately

df['Job'].value_counts().head(3) #top 3 job titles

df[df['Lot']=='90 WT']['Purchase Price']

df[(df['CC Provider']=='Mastercard') & (df['Purchase Price'] > 80)].count() #people made purchase above 80$ with Mastercard
