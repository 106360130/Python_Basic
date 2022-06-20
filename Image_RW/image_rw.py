import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')

plt.imshow(img)
plt.show()

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

