"""
Using simple NumPy operations for manipulating images
=====================================================

This script illustrates how to use basic NumPy operations, such as slicing,
masking and fancy indexing, in order to modify the pixel values of an image.
"""

import numpy as np
from skimage import data
import matplotlib.pyplot as plt

camera = data.camera()

# or, if you want to use imread() from matplotlib
# suppose you have added the "skimage\data" folder into Python's path
#
# import matplotlib.image as mpi
# camera = mpi.imread('camera.png')
#
# refer to "https://matplotlib.org/stable/api/pyplot_summary.html"
# for a catalogue of matplotlib functions

camera[:10] = 0
mask = camera < 87
camera[mask] = 255

d=len(camera)
#print(d)

inds_x = np.arange(d)
inds_y = (4 * inds_x) % d
camera[inds_x, inds_y] = 0

l_x, l_y = camera.shape[0], camera.shape[1]
X, Y = np.ogrid[:l_x, :l_y]
outer_disk_mask = (X - l_x / 2)**2 + (Y - l_y / 2)**2 > (l_x / 2)**2
camera[outer_disk_mask] = 0

plt.figure(figsize=(4, 4))
plt.imshow(camera, cmap='gray')
plt.axis('off')
plt.show() # note that Python shell will not return untill you close the image window


