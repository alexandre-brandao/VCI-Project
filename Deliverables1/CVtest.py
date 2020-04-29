import numpy as np
import cv2 as cv

#Load a color image in grayscale
img = cv.imread('construcsite.jpg', 0)
# imread as the abilities to edit multiple functions
cv.imshow('image', img)# This will display our image
cv.waitKey(0) # 0milliseconds until  input
cv.destroyAllWindows() #Same function as clear
