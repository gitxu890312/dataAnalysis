import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('demo_duplicate.csv')

del df['Unnamed: 0']
print(df)

#占用空间
print(df.size)
print(df.shape)

print(df['Seqno'].duplicated())

s1 = df['Seqno']
print(s1.duplicated())

print(s1.drop_duplicates(keep='last'))

#根据某列去重
df1 = df.drop_duplicates(['Seqno'],keep='last')
print(df1.head())
