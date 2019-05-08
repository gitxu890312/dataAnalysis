
import numpy as np


list_1 = [1,2,3,4]
print(list_1)

array_1 = np.array(list_1)
print(array_1)
print(array_1.dtype)
print(array_1.shape)
print(array_1.ndim)
print(array_1.size)
print("----------------")
list_2 = [5,6,7,8]
array_2 = np.array([[1.0,2,3,4],[5,6,7,8]])
# array_2 = np.array([list_1,list_2])
print(array_2)
print(array_2.dtype)
print(array_2.shape)
print(array_2.size)
print(array_2.ndim)

array_4 = np.arange(1,10,2)
print(array_4)
print(np.zeros(5))
print(np.zeros([2,3]))

print(np.eye(5))
print(np.eye(5).dtype)

a = np.arange(1,10)
print(a[1])
print(a[1:5])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b[1][0])
print(b[:2,1:])