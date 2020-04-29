import numpy as np
import cv2 as cv

#Load a color image in grayscale
img = cv.imread('construcsite.jpg', 0)
cv.imshow('image', img)

k = cv.waitKey(0)

if  k == 27:    #Wait for ESC to EXIT
    cv.destroyAllWindows()
elif k == ord('s'): #wait for 's' key to save and EXIT
    cv.imwrite('construcsite_grey.jpg', img)
    cv.destroyAllWindows()
