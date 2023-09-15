import numpy as np
import matplotlib.pyplot as plt

def conv_table(x, h):
    L_x = len(x)
    L_h = len(h)
    L_y = L_x + L_h - 1
    y = np.zeros(L_y)
    for m in range(L_x):
        for n in range(L_h):
            y[m+n] += h[n] * x[m]
    return L_y, y

n = np.arange(-10, 11)        # Range of results
n1 = np.arange(-20, 21)
h = np.zeros(21)              # Add elements of h(n) to array
for i in range(len(h)):
    h[i] = np.exp(-n[i])

x = np.zeros(21)              # Add elements of x(n) to array
for i in range(len(x)):
    if (i < 11) or (i > 16):
        x[i] = 0
    else:
        x[i] = 1

L_y, y = conv_table(x, h)     # Convolution of h(n) & x(n) by Convolution Table
y1 = np.convolve(x, h)        # Double check by using conv()

plt.figure()
plt.subplot(411)
plt.stem(n, h, 'C0', markerfmt='C0o', label='h(n)')
plt.grid(True)
plt.legend()

plt.subplot(412)
plt.stem(n, x, 'C1', markerfmt='C1o', label='x(n)')
plt.grid(True)
plt.legend()

plt.subplot(413)
plt.stem(n1, y, 'C2', markerfmt='C2o', label='y(n) by self-convolution')
plt.grid(True)
plt.xlim([-10, 10])
plt.legend()

plt.subplot(414)
plt.stem(n1, y1, 'C3', markerfmt='C3o', label='y(n) by conv')
plt.grid(True)
plt.xlim([-10, 10])
plt.legend()

plt.show()
