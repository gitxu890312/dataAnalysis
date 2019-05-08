import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame([["A",1],["B",2],["C",3]],columns=["c1","c2"])
print(df1)

df2 = DataFrame([["C",4],["D",5],["E",6]],columns=["c1","c3"])

print(df2)


df3 = pd.merge(df1,df2)
print(df3)

print("-----left----------")
df4 = pd.merge(df1,df2,how='left')
print(df4)

print("-----right----------")
df4 = pd.merge(df1,df2,on='c1',how='right')
print(df4)

print("--------outer-------")
df4 = pd.merge(df1,df2,on='c1',how='outer')
print(df4)