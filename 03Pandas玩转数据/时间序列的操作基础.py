import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime

t1 = datetime(2016,10,5)
print(t1)

date_list = [
    datetime(2015,9,1),
    datetime(2015,9,10),
    datetime(2016,10,10),
    datetime(2016,10,12),
    datetime(2017,10,12)]

print(date_list)

s1 = Series(np.random.randn(5),index=date_list)
print(s1)
print(s1[1])
print(s1['2015-09-10'])
print(s1['2015-09'])
print(s1['2017'])

s1[1]=22
print(s1)

#生成一个时间数组
date_list = pd.date_range('2016-01-01',freq='D',periods=100)
print(date_list)

s1 = Series(np.random.randn(100),date_list)
print(s1)
