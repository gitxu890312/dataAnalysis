import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

date_range = pd.date_range('2016-01-01',periods=366)
print(date_range)

s1 = Series(np.random.randn(len(date_range)),index=date_range)

print(s1['2016-01'].mean())

#按月取样
s1_month = s1.resample(rule='M').mean()
print(s1_month)
print(type(s1_month))
# s1_month.plot()
# plt.show()
# print(s1)

#按小时取样，并填充数据
s1.resample('H').bfill()
# print(s1.resample('H').ffill())

date_range = pd.date_range('2016-01-01','2016-12-31')
stock_data = DataFrame(index=date_range)
stock_data['BABA'] = np.random.randint(50,200,size=len(date_range))
stock_data['APPLE'] = np.random.randint(500,800,size=len(date_range))


stock_month = DataFrame()
stock_month['BABA'] = stock_data['BABA'].resample('M').mean()
stock_month['APPLE'] = stock_data['APPLE'].resample('M').mean()
stock_month.plot()
plt.show()
