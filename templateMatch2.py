import numpy as np
import cv2

img = cv2.imread('openCV_project/assets/mk11Full.jpeg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('openCV_project/assets/doubleDots2.png', cv2.IMREAD_UNCHANGED)


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
