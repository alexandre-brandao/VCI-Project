import numpy as np
import cv2 as cv

# Declarations
img = cv.imread('WalterWhite.jpg')

#Tests
px = img[100,100]; print(px)
blue = img[100,100,0]; print(blue)

cv.imshow('Walter White', img)
cv.waitKey()