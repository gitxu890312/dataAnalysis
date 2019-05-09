import numpy as np
import pandas as pd
from pandas import Series, DataFrame

score_list = np.random.randint(40,100,size=20)
print(score_list)

bins = [40,60,70,90,100]

#数据分箱
score_cat = pd.cut(score_list,bins)
print(score_cat)

#获取分箱统计数据
s1 = pd.value_counts(score_cat)
print(type(s1))
print(s1)

df = DataFrame()

df['score'] = score_list
df['student'] =[pd.util.testing.rands(3) for i in range(20)]
df = df.sort_values(['score'],ascending=False)

df['cate'] = pd.cut(df['score'],bins,labels=['LOW','ok','GOOD','GREAT'])

print(df)