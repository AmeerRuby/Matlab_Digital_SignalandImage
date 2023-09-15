import numpy as np

def code_seq(b, q):
    if b == 0:
        a = '000 '
        lev = 0
    elif b == q:
        a = '001 '
        lev = 1
    elif b == 2 * q:
        a = '010 '
        lev = 2
    elif b == 3 * q:
        a = '011 '
        lev = 3
    elif b == -q:
        a = '101 '
        lev = -1
    elif b == -2 * q:
        a = '110 '
        lev = -2
    elif b == -3 * q:
        a = '111 '
        lev = -3
    else:
        a = '100 '
        lev = -4
    return a, lev

# Original Signal
t = np.arange(0, 1.01, 0.01)
x_t = 8 * np.cos(4 * np.pi * t)

# Number of Quantization Level
Q = 2

# Sampled Signal
n = np.arange(1, 101)
Ts = 0.01
x_nTs = 8 * np.cos(4 * np.pi * n * Ts)
rep = -99

# Quantized Signal
x_q = np.zeros(x_nTs.shape)
for i in range(len(x_nTs)):
    x_q[i] = np.floor((x_nTs[i] / Q))
    x_q[i] = x_q[i] * Q
    a, lev = code_seq(x_q[i], Q)

    # Quantization level and Code Sequence
    if lev != rep:
        print(f"\nLevel {lev} code sequence: {a}", end="")
    rep = lev

    if x_q[i] >= 8:
        x_q[i] = x_q[i] - Q

# Plot
import matplotlib.pyplot as plt
plt.stem(n * Ts, x_nTs - x_q, linefmt='k', markerfmt='ok')
plt.grid(True)
plt.xlabel('n')
plt.ylabel('e(n)')
plt.ylim([0, 3])
plt.title('Quantization Error')
plt.show()
