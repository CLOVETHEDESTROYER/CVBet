import cv2
import numpy as np

img = cv2.imread('openCV_project/images/columbia.png', cv2.IMREAD_COLOR)


cv2.imshow('Image', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()