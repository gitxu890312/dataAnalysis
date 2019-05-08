import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import webbrowser

# link = 'http://pandas.pydata.org/pandas-docs/version/0.20/io.html'
# webbrowser.open(link)

# df1 = pd.read_clipboard()
# print(df1)
#index =False 去掉index
# df1.to_csv('df1.csv',index=False)

df2 = pd.read_csv('df1.csv')
print(df2)

df2.to_excel('df2.xlsx')

#json转换
# json = df2.to_json()
# print(json)
# df3 = pd.read_json(json)
# print(df3)

