import numpy as np
import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt

img = cv.imread('construcsite.jpg')
img1 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(b,g,r) = cv.split(img)

"""
cv.imshow('blue', b)s
cv.imshow('green', g)
cv.imshow('red', r)
"""

# this will expand the color properly over their gamma
equ = cv.equalizeHist(b)
beq = np.hstack((b,equ)) #stacking images side-by-side (BLUE)
equ = cv.equalizeHist(g)
geq = np.hstack((g,equ)) #stacking images side-by-side (GREEN)
equ = cv.equalizeHist(r)
req = np.hstack((r,equ)) #stacking images side-by-side (RED)

cv.imshow('Blue Equalizer', beq)
cv.imshow('Green Equalizer', geq)
cv.imshow('Red Equalizer', req)

newimg = np.zeros((667, 2000, 3), 'uint8')

newimg[:,:,0] = beq
newimg[:,:,1] = geq
newimg[:,:,2] = req

#newimg = Image.fromarray(newimg) # to convert it to an image and not just a simple array
cv.imshow('FigureEqualized', newimg)
cv.imshow('Image', img)


while(cv.waitKey(1) != 'q'):
    pass

cv.destroyAllWindows()
