import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0,5.0,0.1)
y = np.sin(x*np.pi)

# plt.subplot(2,2,1)# 211设置plot画布为2行1列的画布；当前绘制的为第一个画布
# plt.plot(x,y,'r--')
# plt.ylabel('y1')
# plt.subplot(2,2,4)## 211设置plot画布为2行1列的画布；当前绘制的为第2个画布
# plt.plot(x,y,'g--')
# plt.ylabel('y2')
# plt.subplot(2,2,2)
# plt.plot(x,y,'b--')
# plt.ylabel('y3')
# plt.show()

#canvs为画布
#ax为画布的查分区域数组 2*2的数组
canvs,ax = plt.subplots(2,2)
# canvs.show()
# print(canvs)
ax[0][0].plot(x,y,'r--')
ax[1][1].plot(x,y,'g--')
plt.show()
print(ax)