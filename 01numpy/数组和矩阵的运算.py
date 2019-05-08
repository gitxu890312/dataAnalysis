import numpy as np

print(np.random.randn(5))
#生成一个10以内的随机数
print(np.random.randint(10))

#生成一个大小为20的数组，元素的是小于10的随机数
print(np.random.randint(10,size=20))

#生成一个4*5的随机二维数组
print(np.random.randint(10,size=20).reshape(4,5))

print("-------------")
a = np.random.randint(1,10,size=20).reshape(4,5)
b = np.random.randint(1,10,size=20).reshape(4,5)
print(a)
print(b)
print(type(b))
#数组的加减乘除 对应元素的加减乘除
print("----result------")
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("-------数组转为矩阵-------")
A = np.mat(a)
B = np.mat(b)
print(type(A))
print(type(B))
print(A+B)
print(A-B)
C = np.mat([[1,2,3,4],[5,6,7,8]])
print(C )
print(type(C))
print(C.size)
print(C.shape)
print(C.dtype)
print("--------------矩阵的乘法： 第一个矩阵的列数=第二个矩阵的行数---------------")
A = np.mat(np.random.randint(1,10,size=20).reshape(4,5))
B = np.mat(np.random.randint(1,10,size=20).reshape(5,4))
print(A*B)

print("---------数组常用函数----------")
a = np.random.randint(1,10,size=20).reshape(4,5)
print(a)
print(np.sum(a))#求和
print(np.unique(a))#将数组的值去重
print(np.sum(a[0]))#第一行的和
print(np.sum(a[:,1]))#第一列的和

print(np.max(a))
print(np.max(a[0]))
print(np.max(a[:,1]))

print(a[:,0:4])
