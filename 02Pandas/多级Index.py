import numpy as np
import pandas as pd
from pandas import Series,DataFrame

s1 = Series(np.random.randn(6),index=[['1','1','1','2','2','2'],['a','b','c','a','b','c']])
print(s1)

print(s1['1'])
print(s1['1']['a'])
print(type(s1['1']))
print("-------")
print(s1[:,'a'])

print("----多层index转dataFrame---")
df1 = s1.unstack()
print(df1)
df2 = DataFrame([s1['1'],s1['2']])
print(df2)

print("---------dataFrame转多层index Series--------")
s2 = df1.unstack()
print(s2)

print(df1.T.unstack())

print("--------多层的DataFrame----------")

df2 = DataFrame(np.arange(16).reshape(4,4),index=[['a','a','b','b'],[1,2,1,2]],columns=[['BJ','BJ','JL','JL'],['丰台','朝阳','四平','长春']])
print(df2)
#按照列获取DataFrame
print(df2['BJ','丰台'])
print(type(df2['BJ','丰台']))