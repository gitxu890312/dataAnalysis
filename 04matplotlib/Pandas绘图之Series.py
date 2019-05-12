import numpy as np
import pandas as pd
from  pandas import Series
import matplotlib.pyplot   as plt

# 绘制两条线
s1 = Series(np.random.randn(1000)).cumsum()
s2 = Series(np.random.randn(1000)).cumsum()
# s1.plot(kind='line',grid=True,label='s1',title = 'this is title',style='--')
# s2.plot()
# plt.legend()
# plt.show()

fig,ax = plt.subplots(2,1)
print(fig)
print(ax)

# ax[0].plot(s1)
# ax[1].plot(s2)
# plt.legend()
# plt.show()


#绘制两个不一样的图形
s1[0:10].plot(ax=ax[0],kind='bar')
s2.plot(ax=ax[1])
plt.show()

