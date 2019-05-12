import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

s1 = Series(np.random.randn(1000))

#绘制直方图
# plt.hist(s1,rwidth=0.9,color='r',bins=20)
# plt.show()

#密度图

s1.plot(kind='kde')
plt.show()