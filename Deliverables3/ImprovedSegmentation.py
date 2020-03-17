import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# Ball
BALL_UPPER = np.array([35, 220, 235])
BALL_LOWER = np.array([25, 160, 135])

# FIELD LINES
FIELD_UPPER = np.array([180, 101, 226])
FIELD_LOWER = np.array([8, 0, 174])

##PLAYERS
# RED
RED_UPPER = np.array([11, 255, 255])
RED_LOWER = np.array([0, 87, 92])

# BLUE
BLUE_UPPER = np.array([102, 224, 255])
BLUE_LOWER = np.array([86, 125, 75])


def nothing(x):
    pass


img = cv.imread('CAMBADAFIELD2.png')
img = cv.resize(img, (1366, 768), interpolation=cv.INTER_AREA)

#  Blur the image
blur = cv.GaussianBlur(img, (7, 7), 0)
# blur = cv.medianBlur(img, 6)
#  Obtain HSV image
frame_gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
frame_HSV = cv.cvtColor(blur, cv.COLOR_BGR2HSV)
while 1:


    frame_mask_BALL = cv.inRange(frame_HSV, BALL_LOWER, BALL_UPPER)
    frame_mask_BLUEPlayer = cv.inRange(frame_HSV, BLUE_LOWER, BLUE_UPPER)
    frame_mask_REDPlayer = cv.inRange(frame_HSV, RED_LOWER, RED_UPPER)
    frame_mask_FIELDLINES = cv.inRange(frame_HSV, FIELD_LOWER, FIELD_UPPER)
    mask = frame_mask_BALL + frame_mask_BLUEPlayer + frame_mask_REDPlayer + frame_mask_FIELDLINES

    k = cv.waitKey(1) & 0xFF

    #  Set threshold limits
    ret, frame_masked = cv.threshold(frame_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    frame_masked = cv.bitwise_not(frame_masked)
    frame_masked = frame_masked + mask
    frame_masked = cv.bitwise_and(img, img, mask=frame_masked)

    cv.imshow('Masked', frame_masked)
    cv.imshow('original', img)

    if k == 27:
        break
