import pickle
import numpy as np

x = (np.arange(10))
print(x)

f = open("x.pkl",'wb')
#序列化数组
pickle.dump(x,f)
f = open("x.pkl",'rb')
#反序列化数组
x1 = pickle.load(f)
print(x1)
print(type(x1))

print("--------numpy序列化---------")

np.save("one_array",x)

x2 = np.load("one_array.npy")
print(x2)
print(type(x2))

y = np.arange(20)
print(y)

np.savez("two_array",a=x,b=y)

c = np.load("two_array.npz")
print(type(c))
print(c['a'])
print(c['b'])
