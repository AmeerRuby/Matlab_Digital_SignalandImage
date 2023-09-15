import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

## a) Frequency Response
n = np.array([0.1, 0.1, 0.18, 0.18, 0.09, 0.09])
d = np.array([1, -1.5, 2.2, -1.5, 0.8, 0.18])
w, h = signal.freqz(n, d, 500)
plt.plot(w, abs(h), 'r')
plt.grid(True)
plt.legend(['Frequency response'])
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.show()

## b) Impulse Response
plt.figure()
t, y = signal.dimpulse((n, d, 500))
plt.stem(t, y, use_line_collection=True)
plt.grid(True)
plt.legend(['Impulse response'])
plt.show()

## c) Step Response
s = signal.dstep((n, d, 500))
plt.figure()
plt.plot(s[0], s[1], color=[0.3010, 0.7450, 0.9330])
plt.grid(True)
plt.legend(['Step response'])
plt.show()
