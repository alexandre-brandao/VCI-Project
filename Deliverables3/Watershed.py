import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def nothing(x):
    pass


# Ball
BALL_UPPER = np.array([35, 220, 235])
BALL_LOWER = np.array([25, 160, 135])

# FIELD LINES
FIELD_UPPER = np.array([119, 89, 237])
FIELD_LOWER = np.array([77, 5, 167])

##PLAYERS
# RED
RED_UPPER = np.array([11, 255, 255])
RED_LOWER = np.array([0, 87, 92])

# BLUE
BLUE_UPPER = np.array([102, 224, 255])
BLUE_LOWER = np.array([86, 125, 75])


img = cv.imread('CAMBADAFIELD2.png')
img = cv.resize(img, (1366, 768), interpolation=cv.INTER_AREA)

#  Blur the image
blur = cv.GaussianBlur(img, (5, 5), 0)
# blur = cv.medianBlur(img, 5)
#  Obtain HSV image

frame_HSV = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
while 1:

    k = cv.waitKey(1) & 0xFF

    #  Set Limits for MASKs
    frame_mask_BALL = cv.inRange(frame_HSV, BALL_LOWER, BALL_UPPER)
    frame_mask_BLUEPlayer = cv.inRange(frame_HSV, BLUE_LOWER, BLUE_UPPER)
    frame_mask_REDPlayer = cv.inRange(frame_HSV, RED_LOWER, RED_UPPER)
    frame_mask_FIELDLINES = cv.inRange(frame_HSV, FIELD_LOWER, FIELD_UPPER)
    frame_mask = frame_mask_BALL + frame_mask_BLUEPlayer + frame_mask_REDPlayer + frame_mask_FIELDLINES

    # noise removal
    kernel = np.ones((2, 2), np.uint8)
    opening = cv.morphologyEx(frame_mask, cv.MORPH_OPEN, kernel, iterations=1)


    # sure background area
    sure_bg = cv.dilate(opening, kernel, iterations=5)

    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]

    cv.imshow('Masked', unknown)
    cv.imshow('original', img)
    cv.imshow('blur', blur)
    cv.imshow('Sure Foreground', sure_fg)
    cv.imshow('Sure Background', sure_bg)

    if k == 27:
        break


