import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#apply可以对DataFrame的某个列进行批量处理

df = pd.read_csv("apply_demo.csv")
print(df.head())
print(df.size)

s1 = Series(['a']*df.size)
df['A'] = s1
df['A'] = df['A'].apply(str.upper)

def apply_df(line):
    items = line.strip().split(' ')
    return Series([items[1],items[3],items[5]])
#对dataFrame的某个列进行批量处理 生成一个 新的DataFrame
df_tmp = df['data'].apply(apply_df)
df_tmp = df_tmp.rename(columns={0:"Symbol", 1:"Seqno", 2:"Price"})
print(df_tmp.head())
print(type(df_tmp))
df_new = df.combine_first(df_tmp)
#删除dataFrame的某个列
del df_new['data']
del df_new['A']

print(df_new.head())

df_new.to_csv('demo_duplicate.csv')
