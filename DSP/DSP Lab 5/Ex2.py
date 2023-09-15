import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# a) Stability of the system
n = [8, 10, -6]
d = [1, 2, -1, -2]
z, p, _ = signal.tf2zpk(n, d)
plt.scatter(np.real(p), np.imag(p), marker='x', color='r')
plt.scatter(np.real(z), np.imag(z), marker='o', edgecolors='r', facecolors='none')
plt.grid(True)
plt.show()

# b) Transfer Function in zero-pole-gain form
Ts = 0.5
H1 = signal.TransferFunction(n, d, dt=Ts)
print(H1)

# c) Transfer Function in partial fraction form
r, p, _ = signal.residue(n, d)
H2 = signal.TransferFunction(r, np.poly(p))
print(H2)
