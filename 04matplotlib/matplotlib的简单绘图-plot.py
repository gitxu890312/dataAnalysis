import numpy as np
import  pandas as pd
from pandas import Series,DataFrame

import matplotlib.pyplot as plt

a = [1,2,3]
b = [4,5,6]
# plt.plot(a)
# image = plt.plot(a,b) #绘制单曲线
# image = plt.plot(a,b,'r--') #设置图形的样式
c = [7,8,9]
d = [10,6,8]
# image = plt.plot(a,b,'b--',c,d,'g*') #绘制两个曲线
# print(type(image))
# plt.show()


x = np.arange(0,2.0,0.1)
print(x)
print(x.shape)

y = np.sin(x*np.pi)
x1 = x*2
plt.plot(x,y,'r--',label='aaaa')
plt.plot(x*2,y,'g--',label='bbbb')
plt.xlabel('this is xlabel')
plt.ylabel('this is ylabel')
plt.title('this is title')
plt.legend()
plt.show()


