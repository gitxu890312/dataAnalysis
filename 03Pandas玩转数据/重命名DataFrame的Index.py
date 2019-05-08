import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(9).reshape(3,3),index=["r1","r2","r3"],columns=["A","B","C"])

print(df1)
print(df1.index)
df1.index = Series(["BJ","SH","GZ"])
print(df1)
print(df1.index)

#将index转为小写lower是一个函数
df1.index=df1.index.map(str.lower)
print(df1.index)
print(df1)

#rename原来的dataframe不变，会重新生成一个dataframe
df2 = df1.rename(index={"bj":"beijing"},columns={"A":"a"})
print(df1)
print(df2)


#map函数 将list_1转为list_2的几种方式
list_1 = [1,2,3,4]
list_2 = ['1','2','3','4']

list_3 = [str(x) for  x in list_1]
print(list_3)

list_4 = list(map(str,list_1))
print(list_4)

def map_index(x):
    return x+"_ABC"

tmp = df1.index.map(map_index)
print(tmp)

df2 = df1.rename(index=map_index)
print(df2)

