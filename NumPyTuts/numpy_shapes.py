import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)

b = a.reshape(3,2)
print(b)
print(b.shape)

a = np.arange(24)
print(a)

b = a.reshape(2,4,3)
print(b)

x = np.array([1,2,3,4,5], dtype = np.float32)
print(x.itemsize)
print(x.flags)
