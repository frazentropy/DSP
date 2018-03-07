# Brandt Frazier
# 2018-02-13
# dtmf.py
# Implements a set of bandpass filters to determine numbers corresponding
# to DTMF signals.

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

in_tones = np.loadtxt('./tones.csv', delimiter=',')

# standard keypad constituent tones
# f_r1, f_r2, f_r3, f_r4, f_c1, f_c2, f_c3
f_tones = np.array([697.,770.,852.,941.,1209.,1336.,1477.])

# sample rate
f_s = 8000
samples_per_tone = f_s / 2
num_tones = in_tones.shape[0] / samples_per_tone

in_tones = in_tones.reshape((int(num_tones), int(samples_per_tone)))

# filter length, L, and order, M
L = 64
M = L - 1

n = np.arange(0, L, 1)
h = np.zeros((7, n.shape[0]))

for i in np.arange(0, h.shape[0], 1):
    h[i] = (2/L) * np.cos((2 * np.pi * f_tones[i] * n) / f_s)
x, y = freqz(h[0], 1)
plt.figure(1)
plt.plot(x, abs(y))

y = np.zeros( (h.shape[0], h.shape[1]+int(samples_per_tone)-1) )
y_avg = np.zeros(y.shape[0])
outstring = ""
for i in np.arange(0, in_tones.shape[0], 1):
        for j in np.arange(0, y.shape[0], 1):
            y[j] = np.convolve(h[j], in_tones[i])
        for k in np.arange(0, y_avg.shape[0], 1):
            x, y_freqs = freqz(y[k], 1)
            #plt.figure(2)
            #plt.plot(x, abs(y_freqs))
            y_avg[k] = np.mean(abs(y_freqs))
        rows = y_avg[0:4]
        cols = y_avg[4:]
        row = np.argmax(rows)
        col = np.argmax(cols)
        if (row == 0 and col == 0):
            outstring += "1"
        if (row == 0 and col == 1):
            outstring += "2"
        if (row == 0 and col == 2):
            outstring += "3"
        if (row == 1 and col == 0):
            outstring += "4"
        if (row == 1 and col == 1):
            outstring += "5"
        if (row == 1 and col == 2):
            outstring += "6"
        if (row == 2 and col == 0):
            outstring += "7"
        if (row == 2 and col == 1):
            outstring += "8"
        if (row == 2 and col == 2):
            outstring += "9"
        if (row == 3 and col == 0):
            outstring += "*"
        if (row == 3 and col == 1):
            outstring += "0"
        if (row == 3 and col == 2):
            outstring += "#"

print(outstring)
plt.show()
