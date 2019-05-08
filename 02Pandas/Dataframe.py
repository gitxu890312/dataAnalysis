import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import webbrowser

# link ='https://www.tiobe.com/tiobe-index/'
# webbrowser.open(link)

df1 = pd.read_clipboard()
print(df1)
print(type(df1))

#获取列的title
print(df1.columns)
#获取某一列的数据
print(df1.Ratings)

print(type(df1.Ratings))#Series

df_new = DataFrame(df1,columns=['Programming Language','May 2018'])
print(df_new)

print(df1['May 2018'])#获取某一列

#新增一列
df_new = DataFrame(df1,columns=['Programming Language','May 2018','May 2020'])
print(df_new)

#为新增的一列赋值
# df_new['May 2020'] = np.arange(0,10)
# print(df_new)

# df_new['May 2020'] = range(0,10)
# print(df_new)

# df_new['May 2020'] = pd.Series(np.arange(2,12))
# print(df_new)

#修改指定索引的值
df_new['May 2020'] = pd.Series([100,200],index=[1,2])
print(df_new)