# Brandt Frazier
# 2018-02-13
# pulsecomms.py
# Implements a match filter to recover a string of text from a noisy signal.

import numpy as np
import matplotlib.pyplot as plt

# make numpy array from noisy signal
inData = np.loadtxt('./data-communications.csv', delimiter=',')

# create reference pulses
pulse0 = np.ones(10)
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append(np.ones(5), -1*np.ones(5))
pulse1 = pulse1/np.linalg.norm(pulse1)

# indices where pulses should begin 
indices = np.arange(0, inData.size, 10)

# bits recovered from noisy signal
recoveredBits = np.empty(indices.size, int)

for i, data_i in enumerate(indices):
    inPulse = inData[data_i:data_i+10]
    dot0 = np.inner(inPulse, pulse0)
    dot1 = np.inner(inPulse, pulse1)
    if dot0 > dot1:
        recoveredBits[i] = 0
    else:
        recoveredBits[i] = 1

# indices where bytes begin
indices = np.arange(0, recoveredBits.size, 8)

# bytes to be built from recoveredBits
recoveredBytes = np.zeros(int(recoveredBits.size/8), int)

# radix powers to use for byte conversion
rads = np.power(2*np.ones(8, int),range(8))

for byte_i, bit_i in enumerate(indices):
    for i, b in enumerate(recoveredBits[bit_i:bit_i+8]):
        recoveredBytes[byte_i] += b * rads[7-i]

recoveredBytes = bytearray(recoveredBytes.tolist()).decode('ascii')
print(recoveredBytes)
