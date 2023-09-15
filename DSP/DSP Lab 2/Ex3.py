import numpy as np
import matplotlib.pyplot as plt

def quantized_example(x, R, B):
    Ts = 0.01
    t = np.arange(0, 1+Ts, Ts)
    n = np.arange(1, 100+1, 1)
    A = R/2
    x_nTs = A*np.cos(4*np.pi*n*Ts)
    x_q = np.zeros_like(x_nTs)
    Q = R/(2**B)

    for i in range(len(x_nTs)):
        x_q[i] = np.floor((x_nTs[i] / Q))
        x_q[i] = x_q[i] * Q
        if (x_q[i] >= A):
            x_q[i] = x_q[i] - Q

    y = x_q
    return y

# main program
plt.close('all')
B = int(input('Enter the number of bits B: '))
R = float(input('Enter the range R: '))
Ts = 0.01
t = np.arange(0, 1+Ts, Ts)
n = np.arange(1, 100+1, 1)
A = R/2
x_t = A*np.cos(4*np.pi*t)
x_nTs = A*np.cos(4*np.pi*n*Ts)
x_q = quantized_example(x_t, R, B)

# plot
fig, ax = plt.subplots()
ax.plot(t, x_t, 'k', label='Original Signal')
ax.stem(n*Ts, x_q, 'r', markerfmt='C3o', label='Quantized Signal')
ax.set_xlabel('t/n')
ax.set_ylabel('x(t)/x_q(n)')
ax.grid(True)
ax.legend(loc='upper right')
ax.set_title('Original Signal & Quantized Signal')
plt.show()
