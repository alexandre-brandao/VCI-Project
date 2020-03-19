import numpy as np
import os
import cv2 as cv

def resize_images(directory, size):

    i = 0

    for image in os.listdir(directory):
        i = i+1
        img = cv.imread(directory + image)
        cv.imshow('img', img)
        img = cv.resize(img, size, interpolation=cv.INTER_AREA)
        cv.imwrite('../r_CAMBADA/' + str(i)+'.png', img)

resize_images('../CAMBADA/', (80,80))
show_new_img('../r_CAMBADA/')


