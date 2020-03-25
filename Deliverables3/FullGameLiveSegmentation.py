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
FIELD_UPPER = np.array([180, 101, 226])
FIELD_LOWER = np.array([8, 0, 174])

##PLAYERS
# RED
RED_UPPER = np.array([11, 255, 255])
RED_LOWER = np.array([0, 87, 92])

# BLUE
BLUE_UPPER = np.array([102, 224, 255])
BLUE_LOWER = np.array([86, 125, 75])

# Robot Base
ROBOT_UPPER = np.array([64, 255, 57])
ROBOT_LOWER = np.array([0, 0, 0])

cv.namedWindow('image')
cap = cv.VideoCapture('CAMBADA.mp4')

if not cap.isOpened():
        print("Cannot open camera")

while True:

    # Key INPUT
    k = cv.waitKey(30) & 0xFF

    #Capture frame-by-frame
    ret, img = cap.read();

    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame(stream end?). Exiting...")
        break

    #Our operations on the frame come from here
    # Resize
    img = cv.resize(img, (1366, 768), interpolation=cv.INTER_AREA)
    #  Blur the image
    blur = cv.GaussianBlur(img, (5, 5), 0)
    #  Obtain HSV image
    frame_HSV = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    #  Set Limits for MASKs
    frame_mask_BALL = cv.inRange(frame_HSV, BALL_LOWER, BALL_UPPER)
    frame_mask_BLUEPlayer = cv.inRange(frame_HSV, BLUE_LOWER, BLUE_UPPER)
    frame_mask_REDPlayer = cv.inRange(frame_HSV, RED_LOWER, RED_UPPER)
    frame_mask_FIELDLINES = cv.inRange(frame_HSV, FIELD_LOWER, FIELD_UPPER)
    frame_mask_ROBOTBASE = cv.inRange(frame_HSV, ROBOT_LOWER, ROBOT_UPPER)

    # Final mask
    frame_mask = frame_mask_BALL + frame_mask_BLUEPlayer + frame_mask_REDPlayer + frame_mask_FIELDLINES + frame_mask_ROBOTBASE

    kernel = np.ones((4, 4), np.uint8)
    mask = cv.morphologyEx(frame_mask, cv.MORPH_OPEN, kernel)  # CLEAN MASK NOISE
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)  # INCREASE MASK

    # Inverting mask(This shouldn't be here, for testing purposes only
    # mask = cv.bitwise_not(mask)

    frame = cv.bitwise_and(blur, blur, mask=mask)
    B, G, R = cv.split(frame)

    # HSV_IMAGE = cv.merge([H_mat, S_mat, V_mat])
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('image', frame)

    if k == 27:
        break


#When everything is done, release the Capture
cap.release()
cv.destroyAllWindows()
