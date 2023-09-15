from scipy import signal

num = [0, 0.5]
den = [1, -0.1]
G = signal.TransferFunction(num, den)
num = [0, 0.2]
den = [1, -0.4]
F = signal.TransferFunction(num, den)
K = 2

## Transfer Function H(s)
num = [0, K * G.num[0]]
den = signal.convolve([1, -F.den[1]], [1, -G.den[1]])
H = signal.TransferFunction(num, den)

## Inverse Laplace transform of H(s)
t, y = signal.impulse(H)
print(y)
