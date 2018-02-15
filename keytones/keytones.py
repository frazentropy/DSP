# Brandt Frazier
# 2018-02-06
# keytones.py
# Generates tones for first 12 measures of Twinkle, Twinkle Little Star

import numpy as np
import scipy.io.wavfile

def makeNote(keyNum, duration):
    freq = 440*np.power(2,(keyNum-49)/12)
    t = np.linspace(0,0.5,8000*duration)
    A = 100
    B = freq/(2*np.pi) # unnecessary
    y = A*np.cos(freq*t)
    y = np.asarray(y)
    return y

keys = np.array([
    [52, 0.5],  # measure 1
    [52, 0.5],
    [59, 0.5],
    [59, 0.5],
    [61, 0.5],
    [61, 0.5],
    [59, 0.5],
    [59, 0.5],
    [57, 0.5],
    [57, 0.5],
    [56, 0.5],
    [56, 0.5],
    [54, 0.5],    # measure 7
    [54, 0.25],
    [56, 0.25],
    [52, 1.0],
    [59, 0.5],
    [59, 0.5],
    [57, 0.5],
    [57, 0.5],
    [56, 0.5],
    [56, 0.5],
    [54, 0.5],
    [54, 0.5]
])
waveform = np.zeros([1,0])
for row in keys:
    temp = makeNote(row[0], row[1])
    waveform = np.append(waveform, temp)

scipy.io.wavfile.write('twinkle.wav', 8000, waveform)

