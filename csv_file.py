import pandas as pd

# Read CSV-----------------------------------------
df = pd.read_csv("sched.csv")
# print(df.columns.tolist())
# print(df.head())

#reading rows for one column-------------------
# print(df[0:3]['title'])

#Reading certain columns-------------------
#print(df.loc[:,['title','rating','genre']])


#reading certain columns for a range of rows-------------------
# print(df.loc[1:3],['title'],['rating'])







