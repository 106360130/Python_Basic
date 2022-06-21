import numpy as np
import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)
# img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)

print("type(img) : {}".format(type(img)))
print("img.shape : {}".format(img.shape))


cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

