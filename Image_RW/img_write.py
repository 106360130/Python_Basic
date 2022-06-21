import numpy as np
import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

img = img + 50

# cv2.imshow('My Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('lena2.jpg', img)

