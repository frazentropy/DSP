import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.001)

f1 = 2
f2 = 5

y1 = np.cos(2*np.pi*f1*x);
y2 = np.cos(2*np.pi*f2*x);

name1 = "%d Hz cosine" % f1
name2 = "%d Hz cosine" % f2

plt.subplot(3, 1, 1)
plt.plot(x, y1)
plt.title(name1)
plt.xlabel("seconds")

plt.subplot(3, 1, 2)
plt.plot(x, y2)
plt.title(name2)
plt.xlabel("seconds")

plt.subplot(3, 1, 3)
plt.plot(x, y1+y2)
plt.title(name1 + "+" + name2)
plt.xlabel("seconds")

plt.tight_layout()
plt.show()
