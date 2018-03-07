# Brandt Frazier
# 2018-03-07
# lowpassNoiseRemoval.py
# Implements a lowpass filter to remove noise from a music sample

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz
import soundfile as sf

# 1-d array of amplitudes, sample rate from sound file
data, f_s = sf.read('P_9_2.wav')
#plt.figure(2)
#plt.plot(np.arange(0, data.shape[0], 1), data)
# cutoff frequency for lowpass FIR
f_c = 7500

# filter length
L = 101

# filter order
M = L - 1

# transition frequency
f_t = f_c / f_s

# calculate filter weights h(n)
n = np.arange(0, L, 1)
h = np.zeros(L)
for i in n:
    if i == M/2:
        h[i] = 2 * f_t
    else:
        h[i] = (np.sin(2 * np.pi * f_t * (i - M/2)))
        h[i] = h[i] / (np.pi * (i - M/2))
x, y = freqz(h, 1)
plt.figure(1)
plt.plot(x, abs(y))

# calculate Hamming window weights
w = 0.54 - 0.46 * np.cos((2 * np.pi * n) / M)

# calculate final filter weights
w = np.multiply(w, h)
x, y = freqz(w, 1)
plt.figure(1)
plt.plot(x, abs(y))

clean_data = np.convolve(w, data)
#plt.figure(2)
#plt.plot(np.arange(0, clean_data.shape[0], 1), clean_data)
plt.show()

sf.write('cleanMusic.wav', clean_data, f_s)
