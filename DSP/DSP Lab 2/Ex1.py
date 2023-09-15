import numpy as np
import matplotlib.pyplot as plt



def quantize_signal(x, Q):
    # Determine the minimum and maximum values of the signal
    x_min = np.min(x)
    x_max = np.max(x)

    # Determine the range of the quantization levels
    quant_range = x_max - x_min

    # Calculate the size of each quantization level
    delta = quant_range / Q

    # Create an array to store the quantized signal
    x_q = np.zeros_like(x)

    # Quantize each sample in the signal
    for i in range(len(x)):
        quantization_index = int(((x[i] - x_min)-1) / delta)
        x_q[i] = x_min + quantization_index * delta

    return x_q


# Define the original signal
t = np.linspace(0, 1, num=1000)
x = 8 * np.cos(4 * np.pi * t)

# Define the sampling rate and sample the signal
T = 0.01
nT = np.arange(0, 1, T)
xnT = 8 * np.cos(2 * np.pi * nT)

# Quantize the sampled signal
Q = 8
xnT_q = quantize_signal(xnT, Q)

# Plot the original signal, sampled signal, and quantized signal
fig, ax = plt.subplots(3, 1, figsize=(10, 8))

# Plot the original signal
ax[0].plot(t, x)
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Amplitude')
ax[0].set_title('Original Signal')

# Plot the sampled signal
ax[1].stem(nT, xnT)
ax[1].set_xlabel('Sample Index')
ax[1].set_ylabel('Amplitude')
ax[1].set_title('Sampled Signal')

# Plot the quantized signal
ax[2].stem(nT, xnT_q)
ax[2].set_xlabel('Sample Index')
ax[2].set_ylabel('Amplitude')
ax[2].set_title('Quantized Signal')

plt.tight_layout()
plt.show()
