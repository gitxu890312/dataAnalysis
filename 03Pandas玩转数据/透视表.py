import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = pd.read_excel('sales-funnel.xlsx')

print(df.shape)

# pd.pivot_table(df, index=['Manager','Rep'],values=['Price','Quantity'],columns=['Product'], fill_value=0, aggfunc='sum')
#index  根据index分组
#values 根据values选择展示的列

tmp = pd.pivot_table(df,index=['Manager','Rep'],values=['Price','Quantity'],columns=['Product'],aggfunc='sum')
print(type(tmp))
print((tmp))
print((tmp.index))
# print(help(pd.pivot_table))