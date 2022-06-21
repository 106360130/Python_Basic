import numpy as np
import cv2

img = cv2.imread('lena.jpg')

print("img : {}".format(img))
print("type(img) : {}".format(type(img)))


cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

