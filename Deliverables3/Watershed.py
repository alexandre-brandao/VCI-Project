import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Global Variables declaration
regionSelected = False
refPt = []


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


img = cv.imread('CAMBADAFIELD.png')
img = cv.resize(img, (1366, 768), interpolation=cv.INTER_AREA)
cv.namedWindow('image')

# Set Graphs
plt.ion()
fig = plt.figure()
plt.ylabel('Count')
plt.xlabel('Bins')
plt.xlim([0, 256])
plt.show()

# create trackbars for color change
# cv.CreateTrackbar(Trackbarname, windowName, value, count, onchange)
cv.createTrackbar('G_Upper', 'image', 255, 255, nothing)
cv.createTrackbar('G_Lower', 'image', 0, 255, nothing)

# create switch for ON | OFF functionality
cv.setMouseCallback('image', paint)

#  Blur the image

blur = cv.medianBlur(img, 5)
#  Obtain HSV image
frame_gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)

while 1:

    k = cv.waitKey(1) & 0xFF

    #  Get current positions of 3 Track bars Upper thresh Values
    G_t_select_Upper = cv.getTrackbarPos('G_Upper', 'image')
    #  Get current positions of 3 Track bars Lower thresh Values
    G_t_select_Lower = cv.getTrackbarPos('G_Lower', 'image')

    #  Set Limits for MASK
    frame_mask = cv.inRange(frame_gray, G_t_select_Lower, G_t_select_Upper)

    kernel = np.ones((4, 4), np.uint8)
    mask = cv.morphologyEx(frame_mask, cv.MORPH_OPEN, kernel)  # CLEAN MASK NOISE
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)  # INCREASE MASK

    # Inverting mask(This shouldn't be here, for testing purposes only
    # mask = cv.bitwise_not(mask)

    frame = cv.bitwise_and(blur, blur, mask=mask)

    cv.imshow('image', frame)
    cv.imshow('original', img   )

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
