import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = DataFrame(np.random.randint(1,10,size=40).reshape(10,4),columns=['A','B','C','D'])

# 每一列绘制一条曲线
#kind bar  barh  area 样式
#stacked 多个bar叠加
# df.plot(kind='area',stacked=True)
# plt.show()
#获取dataFrame的一行数据
a = df.iloc[5]

# print(a)
# #dataFrame的每一行绘制一条曲线
# for i in df.index:
#     df.iloc[i].plot(label=str(i))
# plt.legend()
# plt.show()

#简单实现 每一行绘制一条曲线
# df.T.plot()
# plt.show()

# 某一列绘制一条曲线
df['A'].plot()
plt.show()

