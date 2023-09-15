import numpy as np
import matplotlib.pyplot as plt

# Given signal

t = np.arange(-np.pi, np.pi, 0.01)
omega_o = float(input("Input omega_o: "))
omega_s = float(input("Input omega_s: "))
x1 = np.cos(omega_o * t)
x2 = np.cos((omega_o + omega_s) * t)

plt.plot(t, x1)
plt.plot(t, x2)
plt.xlabel('t')
plt.ylabel('x1(t), x2(t)')
plt.grid(True)
plt.show()

# Sample rate:
fs = omega_s / (2 * np.pi)
Ts = 1 / fs
n = np.arange(-3, 4)

x1_nTs = np.cos(n * Ts * omega_o)
x2_nTs = np.cos(n * Ts * (omega_o + omega_s))

plt.stem(n, x1_nTs, 'g', markerfmt='go')
plt.stem(n, x2_nTs, 'k', markerfmt='ko')
plt.legend(('x1(t)', 'x2(t)', 'sampled data'))
plt.xlabel('n')
plt.ylabel('x1(nTs), x2(nTs)')
plt.grid(True)
plt.show()




