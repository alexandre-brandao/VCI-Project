import cv2 as cv
import numpy as np

def nothing(x):
    pass


click = False

def paint(event, x,y,  flags, param): # these parameters are fixed
    global click

    if event == cv.EVENT_LBUTTONDOWN:
        click = True

    if event != cv.EVENT_LBUTTONUP and click:
        cv.circle(img, (x, y), radius, (B, G, R), -1)

    if event == cv.EVENT_LBUTTONUP:
        click = False

# Create a black image, a window
img = np.zeros((300, 512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('Brush radius', 'image', 0, 30, nothing)

# create switch for ON | OFF functionality
switch = '0 : OFF \n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)
cv.setMouseCallback('image', paint)


while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of 5 trackbars
    R = cv.getTrackbarPos('R', 'image')
    G = cv.getTrackbarPos('G', 'image')
    B = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')
    radius = cv.getTrackbarPos('Brush radius', 'image')

    if s == 0:
        img[:] = 0;

