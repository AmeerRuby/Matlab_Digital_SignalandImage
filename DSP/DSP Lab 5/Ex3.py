import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

## Calculate poles and zeros of H(z)
n = [1, 0, 1]
d = [1, -1.39, 1.21]
zeros = np.roots(n)
poles = np.roots(d)

## Plot Poles and zeros of H(z)
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
axs[0].plot(np.real(poles), np.imag(poles), '*', np.real(zeros), np.imag(zeros), 'o')
axs[0].set_xlim([-2, 2])
axs[0].legend(['poles', 'zeros'])

## Impulse Response (80 samples)
t, y = signal.dimpulse((n, d, 1), n=80)
axs[1].stem(t, y[0])
axs[1].grid(True)
axs[1].set_xlabel('n')
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Impulse Response')

plt.show()
