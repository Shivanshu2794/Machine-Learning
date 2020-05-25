import pandas as pd
import numpy as np

df=pd.read_csv('headbrain.csv') #reading csv files
df.head(5)

df.to_csv('new_file.txt') # output csv files to other format

# df.read_excel() for accessing excel files
# df.to_excel() 

# data = pd.read_html('https://www.convertcsv.com/html-table-to-csv.htm') # reading html tables
#type(data)

# basic excercise to understand pd operations

df1=pd.read_csv('Salaries.csv')
df1.head(5)

#df1.info()
df1['BasePay'].mean()
df1['OvertimePay'].max()
df1.head(5)

df1[df1['EmployeeName'] == 'GARY JIMENEZ'] # finding particula employee
df1[df1['EmployeeName'] == 'GARY JIMENEZ']['TotalPay']
df1[df1['TotalPay'] == df1['TotalPay'].min()] # finding details of employee with lowest pay 

df1.iloc[df1['TotalPay'].argmax()] # highest paid employee with advance function 

df1.groupby('Year').mean()['BasePay'] # mean basepay for years 

df1['JobTitle'].value_counts().head(3) # top 3 jobs

df1[df1['Year']==2013]['JobTitle'].value_counts().head(3) # top 3 jobs at a particular year


######### find employees who have word captain in their job title 

def check(title):
    if 'captain' in title.lower().split():
        return True
    else:
        return False


df1[df1['JobTitle'].apply(lambda x: check(x))]

#########


