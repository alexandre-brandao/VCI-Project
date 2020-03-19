import numpy as np
import os
import cv2 as cv


def png2jpg(directory):
    i = 0

    for image in os.listdir(directory):
        if '.png' in image:
            i = i + 1
            img = cv.imread(directory + image)
            if i < 10:
                cv.imwrite(directory + '/00' + str(i) + '.jpg', img)
            elif i < 100:
                cv.imwrite(directory + '/0' + str(i) + '.jpg', img)
            elif i < 1000:
                cv.imwrite(directory + '/' + str(i) + '.jpg', img)


png2jpg('keras-frcnn/train/')
png2jpg('keras-frcnn/test/')

