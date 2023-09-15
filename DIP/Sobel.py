import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# Load image as grayscale
img = plt.imread('cameraman copy.tif')

# Apply Sobel filter in x and y directions
sobel_x = ndimage.sobel(img, axis=0)
sobel_y = ndimage.sobel(img, axis=1)

# Compute gradient magnitude
gradient_mag = np.hypot(sobel_x, sobel_y)

# Plot original and edge-detected images
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Image')
axes[1].imshow(gradient_mag, cmap='gray')
axes[1].set_title('Edge-Detected Image')

plt.show()
