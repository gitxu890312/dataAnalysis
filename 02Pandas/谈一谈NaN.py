import numpy as np
import pandas as pd
from pandas import Series,DataFrame

print(np.nan)
print(type(np.nan))

print(1+np.nan)

#NAN in Series
s1 = Series([1,2,np.nan,3,4],index=['A','B','C','D','E'])
print(s1)
print(s1.isnull())
print(s1.notnull())
s2 = s1.dropna()#删除Series中的Nan字段 返回新的Series s1不变
print(s2)
print(s1)


#NAN in DATAFrame
dframe = DataFrame([[1,2,3],[np.nan,4,5],[7,np.nan,8],[np.nan,np.nan,np.nan]])
print(dframe)
print("--------")
#axis = 0,0 按照行删除，1按照列删除
# how = 'any', any只要有一个NAN就删除整行或整列 all 所有的元素都是NAN才删除
# thresh = None,NAN的个数大于thresh时才会删除

print(dframe.dropna())# 主要一行有一个NAN就会删除
print("--------")
print(dframe.isnull())
print("----------")
print(dframe.notnull())
print("------")
print(dframe.dropna(axis=1))
print("------")
print(dframe.dropna(axis=0,how="all"))

#使用指定的值替换NAN
print(dframe.fillna(1))

#第一行用0替换；第二行用1替换 依次类推
print(dframe.fillna(value={0:0,1:1,2:2,3:3}))