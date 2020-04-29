import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Global Variables declaration
regionSelected = False
refPt = []

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


def nothing(x):
    pass


def paint(event, x, y, flags, param):  # these parameters are fixed
    global regionSelected
    global refPt

    if event == cv.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]

    if event == cv.EVENT_LBUTTONUP:
        refPt = refPt.append((x, y))
        regionSelected = True


img = cv.imread('CAMBADA_CLOSEUP.png')
img = cv.resize(img, (1366, 768), interpolation=cv.INTER_AREA)
cv.namedWindow('image')

# create switch for ON | OFF functionality
cv.setMouseCallback('image', paint)

#  Blur the image
blur = cv.GaussianBlur(img, (5, 5), 0)
#  Obtain HSV image
frame_HSV = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

while 1:

    k = cv.waitKey(1) & 0xFF

    #  Set Limits for MASKs
    frame_mask_BALL = cv.inRange(frame_HSV, BALL_LOWER, BALL_UPPER)
    frame_mask_BLUEPlayer = cv.inRange(frame_HSV, BLUE_LOWER, BLUE_UPPER)
    frame_mask_REDPlayer = cv.inRange(frame_HSV, RED_LOWER, RED_UPPER)
    frame_mask_FIELDLINES = cv.inRange(frame_HSV, FIELD_LOWER, FIELD_UPPER)

    # Final mask
    frame_mask = frame_mask_BALL + frame_mask_BLUEPlayer + frame_mask_REDPlayer + frame_mask_FIELDLINES

    kernel = np.ones((4, 4), np.uint8)
    mask = cv.morphologyEx(frame_mask, cv.MORPH_OPEN, kernel)  # CLEAN MASK NOISE
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)  # INCREASE MASK

    # Inverting mask(This shouldn't be here, for testing purposes only
    # mask = cv.bitwise_not(mask)

    frame = cv.bitwise_and(blur, blur, mask=mask)
    B, G, R = cv.split(frame)

    # HSV_IMAGE = cv.merge([H_mat, S_mat, V_mat])
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('image', frame)
    cv.imshow('original', img)

    if regionSelected:
        pass

    if k == 27:
        break

""" INFO
RED
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])

Ball
BALL_UPPER = np.array([033, 200,235])
BALL_LOWER = np.array([027, 160,135])

FIELD LINES
FIELD_UPPER = np.array([119, 089, 237])
FIELD_LOWER = np.array([077, 005, 167])

 PLAYERS
RED
RED_UPPER = np.array([011, 255, 255])
RED_LOWER = np.array([000, 087, 092])

BLUE
BLUE_UPPER = np.array([102, 224, 255])
BLUE_LOWER = np.array([086, 125, 075])
"""
