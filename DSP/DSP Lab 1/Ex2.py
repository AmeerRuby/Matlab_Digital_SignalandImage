import numpy as np
import matplotlib.pyplot as plt

# Part a
# Given the signal:
t = np.arange(0, 2, 0.001)
f1, f2, f3 = 1, 4, 6
x = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t) + np.cos(2*np.pi*f3*t)
x_a = 3*np.cos(2*np.pi*t)
plt.plot(t, x)
plt.grid(True)
plt.plot(t, x_a)
plt.xlabel('t')
plt.ylabel('x(t),x_a(t),x(nT_s)')

# Sample rate:
fs = 5
Ts = 1/fs
n = np.arange(0, 11)

x_nTs = np.cos(n*Ts*2*np.pi*f1) + np.cos(n*Ts*2*np.pi*f2) + np.cos(n*Ts*2*np.pi*f3)


plt.stem(n*Ts, x_nTs, 'r', markerfmt='D')
plt.legend(['x(t)', 'xa(t)', 'sampled data'])

# Part b
f1, f2, f3 = 1, 4, 6
# => f3 outside of Nyquist rate
f3a = f3 - fs/2
x_a = np.cos(2*np.pi*t) + np.cos(8*np.pi*t) + np.cos(2*np.pi*f3a*t)
plt.figure()
plt.plot(t, x)
plt.grid(True)
plt.plot(t, x_a)
plt.xlabel('t')
plt.ylabel('x(t),x_a(t),x(nT_s)')

# Sample rate:
fs = 10
Ts = 1/fs
n = np.arange(0, 21)

x_nTs = np.cos(n*Ts*2*np.pi*f1) + np.cos(n*Ts*2*np.pi*f2) + np.cos(n*Ts*2*np.pi*f3)


plt.stem(n*Ts, x_nTs, 'g', markerfmt='go')
plt.legend(['x(t)', 'xa(t)', 'sampled data'])

plt.show()
