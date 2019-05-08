import numpy as np
import pandas as pd
from pandas import Series,DataFrame

#Series的加法
s1 = Series([1,2,3,4],index=['A','B','C','D'])
s2 = Series([5,6,7,8],index=["C","D","E","F"])
s3 = s1+s2
print(s3)

#DataFrame的运算
df1 = DataFrame(np.arange(4).reshape(2,2),index=["r1","r2"],columns=["c1","c2"])
df2 = DataFrame(np.arange(9).reshape(3,3),index=["r1","r2","r3"],columns=["c1","c2","c3"])
print(df1)
print(df2)
df3 = df1 + df2   #+ - * /  %都可以
print(df3)
#DataFrame的常用函数
df4 = DataFrame([[1,2,3],[4,np.nan,5],[6,7,8]],index=["r1","r2","r3"],columns=["c1","c2","c3"])
print(df4)
print(df4.sum()) #列的和
print(df4.sum(axis=1)) #行的和
print(df4.min())
print(df4.max())

print(df4.describe())


