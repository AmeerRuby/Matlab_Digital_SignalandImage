import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

## a) Calculate poles and zeros of H(z)
n = np.array([1, 0, 1])
d = np.array([1, -1.39, 1.21])
zeros = np.roots(n)
poles = np.roots(d)

## Plot Poles and zeros of H(z)
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
t, y = signal.dimpulse((n, d, 1), n=80)
axs[0].plot(np.real(poles), np.imag(poles), '*', np.real(zeros), np.imag(zeros), 'o')
axs[0].set_xlim([-2, 2])
axs[0].legend(['poles', 'zeros'])

axs[1].step(t, np.squeeze(y))
axs[1].grid(True)
plt.show()

## Impulse Response (80 samples)
t, y = signal.dimpulse((n, d, 1), n=80)
axs[1].step(t, y[:, 0, 0])
axs[1].grid(True)
plt.show()

## a) Transfer Function H_2(z)
n1 = np.array([1, 0, 0])
d1 = np.array([1, 0.2, 0.01])
H2 = signal.TransferFunction(n1, d1, dt=0.5, iodelay=2)

## b) Impulse Response of Transfer Function H_1(z)
fig, ax = plt.subplots(figsize=(10, 5))
t, h1 = signal.dimpulse((n1, d1, 1))
ax.stem(t, h1, use_line_collection=True, label='Impulse Response', basefmt='k')
ax.legend()
ax.grid(True)
plt.show()

## c)Impulse Response of Transfer Function H_2(z)
fig, ax = plt.subplots(figsize=(10, 5))
t, y, _ = signal.dlti(H2.num, H2.den).output(n=80)
ax.stem(t, y, use_line_collection=True, label='Impulse Response', basefmt='k')
ax.legend()
ax.grid(True)
plt.show()
