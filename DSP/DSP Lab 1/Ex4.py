import numpy as np
import matplotlib.pyplot as plt

# a
f = np.zeros(4)
# Input frequencies
for i in range(4):
    f[i] = float(input(f"Enter f{i + 1} = "))

# Plot x_a(t)
t = np.arange(-2, 2.01, 0.01)
x_a = 2.5 * np.cos(2 * np.pi * f[0] * t) - 1.5 * np.sin(2 * np.pi * f[1] * t) + np.cos(
    2 * np.pi * f[2] * t) + 0.5 * np.cos(2 * np.pi * f[3] * t)

plt.figure()
plt.plot(t, x_a, 'k', linewidth=1.5)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('x_a(t)')
plt.title('Signal x_a(t)')
plt.show()

# b
fs1 = 5 * max(f)
Ts1 = 1 / fs1
n1 = np.arange(-np.ceil(t[-1] / Ts1), np.ceil(t[-1] / Ts1) + 1)

x_nTs1 = 2.5 * np.cos(2 * np.pi * f[0] * n1 * Ts1) - 1.5 * np.sin(2 * np.pi * f[1] * n1 * Ts1) + np.cos(
    2 * np.pi * f[2] * n1 * Ts1) + 0.5 * np.cos(2 * np.pi * f[3] * n1 * Ts1)

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, x_a, 'k', linewidth=1.5)
plt.xlabel('t')
plt.ylabel('x_a(t)')
plt.legend(['x_a(t)'])
plt.title('Original Continuous Time Signal x_a(t)')
plt.grid(True)
plt.subplot(3, 1, 2)
plt.stem(n1 * Ts1, x_nTs1, 'b', markerfmt='bo', basefmt=' ')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend(['x[n]'])
plt.title('Sampled Discrete Time Signal x[n]')
plt.grid(True)
plt.subplot(3, 1, 3)
plt.plot(t, x_a, 'r', linewidth=1.5)
plt.stem(n1 * Ts1, x_nTs1, 'g', markerfmt='go', basefmt=' ')
plt.xlabel('t')
plt.ylabel('x[n] and the reconstructed Signal')
plt.legend(['x_a(t)', 'x[n]'])
plt.title('x[n] and the reconstructed Signal')
plt.show()

# c
fs2 = 0.5 * max(f)
Ts2 = 1 / fs2
n2 = np.arange(-np.ceil(t[-1] / Ts2), np.ceil(t[-1] / Ts2) + 1)

x_nTs2 = 2.5 * np.cos(2 * np.pi * f[0] * n2 * Ts2) - 1.5 * np.sin(2 * np.pi * f[1] * n2 * Ts2) + np.cos(
    2 * np.pi * f[2] * n2 * Ts2) + 0.5 * np.cos(2 * np.pi * f[3] * n2 * Ts2)
x_as = 2.5 * np.cos(2 * np.pi * fs2 * t) - 1.5 * np.sin(2 * np.pi * fs2 * t) + np.cos(
    2 * np.pi * fs2 * t) + 0.5 * np.cos(2 * np.pi * fs2 * t)

plt.figure()
plt.subplot(4, 1, 1)
plt.plot(t, x_a, 'k', linewidth=1.5)
plt.xlabel('t')
plt.ylabel('x_a(t)')
plt.legend(['x_a(t)'])
plt.title('Original Continuous Time Signal x_a(t)')
plt.grid(True)
plt.subplot(4, 1, 2)
plt.stem(n2 * Ts2, x_nTs2, 'b', markerfmt='bo', basefmt=' ')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.legend(['x[n]'])
plt.title('Sampled Discrete Time Signal x[n]')
plt.grid(True)
plt.subplot(4, 1, 3)
plt.plot(t, x_a, 'r', linewidth=1.5)
plt.stem(n2 * Ts2, x_nTs2, 'g', markerfmt='go', basefmt=' ')
plt.xlabel('t')
plt.ylabel('x[n] and the reconstructed Signal')
plt.legend(['x_a(t)', 'x[n]'])
plt.title('x[n] and the Original Signal')
plt.grid(True)
plt.subplot(4, 1, 4)
plt.plot(t, x_as, 'k', linewidth=1.5)
plt.stem(n2 * Ts2, x_nTs2, 'g', markerfmt='go', basefmt=' ')
plt.xlabel('t')
plt.ylabel('x[n] and the reconstructed Signal')
plt.legend(['x_a_s(t)', 'x[n]'])
plt.title('x[n] and the reconstructed Signal')
plt.grid(True)
plt.show()




