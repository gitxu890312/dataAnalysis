import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_csv('city_weather.csv')
print(df)
#根据某个列分组
group = df.groupby(['city'])
print(group)
print(group.groups)

print("获取分组后的dataFrame")
df_bj = group.get_group('BJ')
print(type(df_bj))
print(df_bj)
print("---------------")
print(df_bj.mean())
print(type(df_bj.mean()))

print("-------分组函数-------")
#只有可以调用分组函数的列才会显示出来 ，不能执行分组函数的列会被忽略掉
print(group.max())
print(group.max().index)
print(group.max().columns)

print("--------将分组转为列表---------")
g_list = list(group)
for i in g_list:
    print(type(i))
    print(len(i))
    print(type(i[0]))
    print(type(i[1]))
    break
print("-----分组转dict-------")
g_dic = dict(list(group))
print(type(g_dic))



