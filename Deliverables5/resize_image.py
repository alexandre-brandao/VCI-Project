import numpy as np
import os
import cv2 as cv

def resize_images(directory, size):


    for image in os.listdir(directory):
        if '.jpg' in image:
            print("Found" + directory+image)
            i = image.split('.')
            img = cv.imread(directory + image)
            cv.imshow('img', img)
            img = cv.resize(img, size, interpolation=cv.INTER_AREA)
            cv.imwrite('../workspace/training_demo/images/' + i[0]+'.jpg', img)
            print("New file ../workspace/training_demo/images/" + i[0]+".jpg\n")

resize_images('../workspace/training_demo/images/', (1280,720))



