import numpy as np
import pandas as pd
from pandas import Series,DataFrame

df = pd.read_csv("city_weather.csv")

group_city = df.groupby(['city'])
#系统分组函数
df_min = group_city.agg('min')
print(df_min)
print("---------------")
def foo(attr):
    # print(type(attr)) #Series
    # print(attr)
    return attr.max() - attr.min()

df_city = group_city.agg(foo)
# print(df)

df_new = df.groupby(['city','wind'])
print(df_new)
# print(df_new.value_counts())
print(df_new.get_group(('BJ',3)))
for (name_1,name_2), group in df_new:
    print(name_1,name_2)
    print(group)
