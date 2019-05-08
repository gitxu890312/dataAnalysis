import pandas as pd
import numpy as np

#pandas序列
s1 = pd.Series([1,2,3,4])
print(s1)
print(s1.shape)
print(s1.dtype)
print(type(s1))
print(s1.index)
print(s1.values)

s2 = pd.Series({"name":'张三',"age":14,"address":"北京"})
print(s2)
print(s2.index)
print(s2.values)


s3 = pd.Series({'A':1,'B':2,"C":3,"D":4})
print(s3.index)
print(s3.values)
index_1 = ['A','B','C','D','E']
#Series 复制
s4 = pd.Series(s3,index=index_1)

print(s4)
print(s4['E'])
print(np.isnan(s4))

#Series转字典
print(s4.to_dict())
print(type(s4.to_dict()))

#初始化Series
s5 = pd.Series([1,2,3,4],index=["C","D","E","F"])
print(s5)
print(s5[s5>=3])#获取value大于等于3的entry

