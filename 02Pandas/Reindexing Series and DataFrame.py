import numpy as np
import pandas as pd
from  pandas import Series,DataFrame

s1 = Series([1,2,3,4],index=['A','B','C','D'])
print(s1)
#重新设置Series的index
print(s1.reindex(['A','B','C','D','E','F']))
print(s1.reindex(['A','D','E','F']))

#重新设置Series 的index 并为新的index设定指定值
print(s1.reindex(['A','D','E','F'],fill_value=10))


s2 = Series(['A','B','C'],index=[1,5,10])
print(s2)

#1-5设为A 5-10设为B >10设为C
print(s2.reindex(np.arange(0,10),method='ffill'))

df1 = DataFrame(np.random.randint(10,size=25).reshape(5,5),index=["1","2",'4',"5","6"],columns=["A","B","D","E","F"])
print(df1)

df2 = df1.reindex(index=["1","2",'3','4',"5","6"],columns=["A","B","C","D","E","F"])
print(df2)

print(df1.reindex(index=["1","2"],columns=["A","B"]))

print(s1)
#删除Series指定索引
print(s1.drop('A').drop('B'))
# 删除DataFrame行
print(df1.drop('1').drop('2'))
#删除DataFrame列
print(df1.drop('A',axis=1))

