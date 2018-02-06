import numpy as np
x = np.empty([3,2], dtype=int)
print(x)

x = np.zeros(5)
print(x)

x = np.zeros((5,), dtype = np.int)
print(x)

x = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)

x = np.ones(5)
print(x)

x = np.ones([2,2], dtype = int)
print(x)

# convert list to ndarray
x = [1,2,3]
a = np.asarray(x)
print(a)

# dtype is set
x = [1,2,3]
a = np.asarray(x, dtype = float)
print(a)

# ndarray from list of tuples
x = [(1,2,3),(4,5)]
a = np.asarray(x)
print(a)

# from buffer (doesn't work in py3)
#s = 'Hello World'
#a = np.frombuffer(s, dtype = 'S1')
#print(a)

# from iterable object
list = range(5)
it = iter(list)
x = np.fromiter(it, dtype=float)
print(x)


