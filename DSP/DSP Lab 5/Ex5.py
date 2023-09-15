import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

## Calculate poles and zeros of H(z)
n = [1, 0, 1]
d = [1, -1.39, 1.21]
zeros = np.roots(n)
poles = np.roots(d)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

## a) x[n] is the unit impulse sequence
axs[0].set_title('Impulse Response')
t, y = signal.dimpulse((n, d, 1), n=100)
axs[0].step(t, y[:, 0, 0])
axs[0].grid(True)

## b) x[n] is the unit step sequence
axs[1].set_title('Step Response')
t, y = signal.dstep((n, d, 1), n=100)
axs[1].step(t, y[:, 0, 0])
axs[1].grid(True)

plt.show()


plt.show()
