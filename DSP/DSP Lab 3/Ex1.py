import numpy as np
import matplotlib.pyplot as plt

# a)
x1 = int(input('Input number of elements in x(n): '))
h1 = int(input('Input number of elements in h(n): '))

x = np.zeros(x1)
h = np.zeros(h1)

for i in range(x1):
    x[i] = float(input('Input element of x(n): '))

for i in range(h1):
    h[i] = float(input('Input element of h(n): '))

print('Convolution of x(n) and h(n) = ')
y = np.convolve(x, h)

# b)
n = np.arange(-15, 16)
h = np.zeros(31)

for i in range(len(h)):
    if i < 16 or i > 21:
        h[i] = 0
    else:
        h[i] = 2**n[i]

x = np.zeros(31)

for i in range(len(x)):
    if i < 6 or i > 21:
        x[i] = 0
    else:
        x[i] = 1 * (n[i] >= -10) - 1 * (n[i] >= 5)

y1 = np.convolve(x, h, mode='same')

plt.subplot(211)
plt.stem(n, h, use_line_collection=True, markerfmt='bo', basefmt='b-')
plt.grid(True)
plt.title('h(n)')
plt.xlabel('n')
plt.ylabel('h(n)')

plt.subplot(212)
plt.stem(n, x, use_line_collection=True, markerfmt='ro', basefmt='r-')
plt.grid(True)
plt.title('x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')

plt.figure()

plt.subplot(211)
plt.stem(n, y1, use_line_collection=True, markerfmt='go', basefmt='g-')
plt.grid(True)
plt.title('y(n) by convolution')
plt.xlabel('n')
plt.ylabel('y(n)')

# c)
X = np.fft.fft(x)
H = np.fft.fft(h)
Y = X * H
y2 = np.fft.ifft(Y)

y3 = np.zeros(31)
for i in range(len(y3)):
    if i < 16:
        y3[i] = y2[i + 15].real
    else:
        y3[i] = y2[i - 15].real

plt.subplot(212)
plt.stem(n, y3, use_line_collection=True, markerfmt='mo', basefmt='m-')
plt.grid(True)
plt.title('y(n) by IFT')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.xlim([-15, 15])

plt.show()

