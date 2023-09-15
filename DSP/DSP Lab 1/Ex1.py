import numpy as np
import matplotlib.pyplot as plt

def sigadd(x1, n1, x2, n2):
    n = np.arange(min(np.min(n1), np.min(n2)), max(np.max(n1), np.max(n2))+1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    y1[np.where(np.in1d(n, n1))] = x1
    y2[np.where(np.in1d(n, n2))] = x2
    y = y1 + y2
    return y, n

def sigfold(x, n):
    y = np.flip(x)
    n = -np.flip(n)
    return y, n

def sigmult(x1, n1, x2, n2):
    n = np.arange(min(np.min(n1), np.min(n2)), max(np.max(n1), np.max(n2))+1)
    y1 = np.zeros(len(n))
    y2 = np.zeros(len(n))
    y1[np.where(np.in1d(n, n1))] = x1
    y2[np.where(np.in1d(n, n2))] = x2
    y = y1 * y2
    return y, n

def sigshift(x, n, k):
    n = n + k
    y = x
    return y, n

# Given signal x(n)
n = np.array([-4,-3,-2,-1,0,1,2])
x = np.array([1,-2,4,6,-5,8,10])
plt.stem(n, x,)
plt.grid(True)
plt.title('Given signal x(n)')
plt.xlabel('n')
plt.ylabel('x')
plt.show()

# a) x1(n) = 3x(n+2) + x(n-4) + 2x(n)
x1_a, n1_a = sigshift(x, n, -2)
x2_a, n2_a = sigshift(x, n, 4)
y1_a, n1_a = sigadd(3*x1_a, n1_a, x2_a, n2_a)
y_a, n_a = sigadd(y1_a, n1_a, 2*x, n)
plt.stem(n_a, y_a, 'g', markerfmt='go')
plt.grid(True)
plt.title('Signal x1[n]')
plt.xlabel('n')
plt.ylabel('x')
plt.show()

# b) x2(n) = 5x(5+n) + 4x(4+n) + 3x(n)
x1_b, n1_b = sigshift(x, n, -5)
x2_b, n2_b = sigshift(x, n, -4)
y1_b, n1_b = sigadd(5*x1_b, n1_b, 4*x2_b, n2_b)
y_b, n_b = sigadd(y1_b, n1_b, 3*x, n)
plt.stem(n_b, y_b, 'r', markerfmt='ro')
plt.grid(True)
plt.title('Signal x2[n]')
plt.xlabel('n')
plt.ylabel('x')
plt.show()

# c) x3(n) = x(n+4)x(n-1) + x(2-n)x(n)
x1_c, n1_c = sigshift(x, n, -4)
x2_c, n2_c = sigshift(x, n, 1)
y1_c, n1_c = sigmult(x1_c, n1_c, x2_c, n2_c)
x3_c, n3_c = sigfold(x, n)
x3_c, n3_c = sigshift(x3_c, n3_c, -2)
y2_c, n2_c = sigmult(x3_c, n3_c, x, n)
y_c, n_c = sigadd(y1_c, n1_c, y2_c, n2_c)
plt.stem(n_c, y_c, 'r', markerfmt='ro')
plt.grid(True)
plt.title('Signal x3[n]')
plt.xlabel('n')
plt.ylabel('x')
plt.show()

# d) x4(n) = 2x(n)+cos(0.1pin)x(n+2) , -10 <= n <= 10
x1_d, n1_d = sigshift(x, n, -2)
n2_d = np.arange(-10, 11)
x2_d = np.cos(0.1 * np.pi * n2_d)
y1_d, n1_d = sigmult(x2_d, n2_d, x1_d, n1_d)
y_d, n_d = sigadd(y1_d, n1_d, 2*x, n)
plt.stem(n_d, y_d, 'r', markerfmt='ro')
plt.grid(True)
plt.title('Signal x4[n]')
plt.xlabel('n')
plt.ylabel('x')
plt.show()



