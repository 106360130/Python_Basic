import numpy as np
import cv2
from matplotlib import pyplot as plt

img_bgr = cv2.imread('lena.jpg')

# BGR to RGB
img_rgb = img_bgr[:,:,::-1]
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
# BGR to RGB

print("type(img_rgb) : {}".format(type(img_rgb)))

plt.imshow(img_rgb)
# plt.imshow(img_rgb[:, :, 1], cmap='gray', vmin = 0, vmax = 255, interpolation = 'none')

plt.show()