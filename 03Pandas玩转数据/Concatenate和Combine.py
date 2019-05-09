import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#concatenate组合
#combine 填充

#数组的concatenate
arr1 = np.mat(np.arange(9).reshape(3,3))
arr2 = np.mat(np.arange(9).reshape(3,3))
print(np.concatenate([arr1,arr2],axis=0))

#Series的concat
s1 = Series(['A','B','C'],index=[1,2,3])
s2 = Series(['D','E','C'],index=[5,6,3])
s3 = pd.concat([s1,s2],axis=0) #axis=1时 扩展为DataFrame axis=0时为Series
print(s3)
print(type(s3))


df1 = DataFrame(np.random.randn(4,3),columns=["X","Y","Z"])
df2 = DataFrame(np.random.randn(4,3),columns=["X","Y","A"])
df3 = pd.concat([df1,df2],axis=0)
print(df3)
print(type(df3))
#For more info in documentation:
url='http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html'

#combine

