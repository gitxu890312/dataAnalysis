import numpy as np
import pandas as pd
from pandas import Series, DataFrame

link = 'https://projects.fivethirtyeight.com/flights/'

df = pd.read_csv('usa_flights.csv')
print(df.values)
print(df.shape)

#1. 获取延误时间最长top10的航空公司
tmp = df.sort_values(['arr_delay'],ascending=False)
tmp = tmp.reindex(columns=['flight_date','unique_carrier','flight_num','origin','dest','arr_delay'])[0:10]
print(tmp)

#2.计算延误和没有延误所占比例
df['delayed'] = df['arr_delay'].apply(lambda x: x > 0)
delay_data = df['delayed'].value_counts() #统计某个列值得个数
res = delay_data[1]/(delay_data[0] + delay_data[1])
print(res)

#3.每一个航空公司延误的情况
delay_group = df.groupby(['unique_carrier','delayed'])
df_delay = delay_group.size().unstack()
print(df_delay)
import matplotlib.pyplot as plt
df_delay.plot(kind='barh', stacked=True, figsize=[16,6], colormap='winter')
# plt.show()

#4. 透视表功能
flights_by_carrier = df.pivot_table(index='flight_date', columns='unique_carrier', values='flight_num', aggfunc='count')
flights_by_carrier.head()