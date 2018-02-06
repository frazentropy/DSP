import numpy as np
x = np.arange(5)
print(x)

# dtype set
x = np.arange(5, dtype=float)
print(x)

# start and stop parameters set
x = np.arange(10,20,2)
print(x)

# linear spacing
x = np.linspace(10,20,5)
print(x)

# endpoint set to false
x = np.linspace(10,20,5, endpoint = False)
print(x)

# find retstep value
x = np.linspace(1,2,5, retstep = True)
print(x)

# logarithmic spacing: default base is 10
a = np.logspace(1.0,2.0, num = 10)
print(a)

# set base of logspace to 2
a = np.logspace(1,10, num = 10, base = 2)
print(a)
