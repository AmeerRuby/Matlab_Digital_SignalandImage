from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

img1 = np.array(Image.open('img1.jpeg'))
figure, plots = plt.subplots(ncols=3, nrows=1)
for i, subplot in zip(range(3), plots):
    temp = np.zeros(img1.shape, dtype='uint8')
    temp[:,:,i] = img1[:,:,i]
    subplot.imshow(temp)
    subplot.set_axis_off()
plt.show()