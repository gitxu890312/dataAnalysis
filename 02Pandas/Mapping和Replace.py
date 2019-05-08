import numpy as np
import pandas as pd
from  pandas import Series,DataFrame

df1 = DataFrame({'城市':['北京','上海','广州'],'人口':[1000,2000,1500]})
print(df1)

# 为DataFrame增加一个Series
# df1['GDP']=Series([1000,2000,1500])
# print(df1)

# GDP_MAP = {'北京':1000,'上海':2000,'广州':1500}
# df1['GDP']=df1['城市'].map(GDP_MAP)
# print(df1)



df1 = DataFrame({'城市':['北京','上海','广州'],'人口':[1000,2000,1500]},index=['A','B','C'])
print(df1)
#Series 的index必须要和DataFrame的index一致
df1['GDP'] = Series([1000,2000,1500],index=['A','B','C'])
print(df1)

print("-------replace in Series---------")

s1 = Series(np.arange(0,10))
print(s1)
# s1[2]=np.nan
# print(s1)

s2 = s1.replace([1,2,3],['aa',20,30])
print(s2)


