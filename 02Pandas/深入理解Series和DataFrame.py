import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data = {'Country': ['China', 'India', 'Brazil'],
    'Capital': ['Beijing', 'New Delhi', 'Brasilia'],
    'Population': ['1432732201', '1303171635', '207847528']}
print(type(data))
print(data)

s1 = Series(data['Country'])
s2 = Series(data['Capital'])
s3 = Series(data['Population'])
print(s1)
print(s2)
print(s3)

df = DataFrame(data)
print(df)
#dataFrame  行的遍历
#每一行是一个长度为2的tuple
#第一个元素为索引
#第二个元素为Series
for i in df.iterrows():
    print(i[0],(i[1]))
    print("-----")

#通过Series创建 dataFrame
df1 = DataFrame([s1,s2,s3] ,index=["Country","Capital","Population"])
print(df1)
# 行列转换
print(df1.T)