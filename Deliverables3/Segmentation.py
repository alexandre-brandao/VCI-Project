import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Global Variables declaration
regionSelected = False
refPt = []

def nothing(x):
    pass


def paint(event, x, y,  flags, param):  # these parameters are fixed
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

# Set Graphs
plt.ion()
fig = plt.figure()
plt.ylabel('Count')
plt.xlabel('Bins')
plt.xlim([0, 256])
plt.show()

# create trackbars for color change
# cv.CreateTrackbar(Trackbarname, windowName, value, count, onchange)
cv.createTrackbar('H_Upper', 'image', 180, 180, nothing)
cv.createTrackbar('H_Lower', 'image', 0, 180, nothing)

cv.createTrackbar('S_Upper', 'image', 255, 255, nothing)
cv.createTrackbar('S_Lower', 'image', 0, 255, nothing)

cv.createTrackbar('V_Upper', 'image', 255, 255, nothing)
cv.createTrackbar('V_Lower', 'image', 0, 255, nothing)

# create switch for ON | OFF functionality
cv.setMouseCallback('image', paint)

#  Blur the image
#blur = cv.GaussianBlur(img, (5, 5), 0)
blur = cv.medianBlur(img, 5)
#  Obtain HSV image
frame_HSV = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

while 1:

    k = cv.waitKey(1) & 0xFF

    #  Get current positions of 3 Track bars Upper thresh Values
    H_t_select_Upper = cv.getTrackbarPos('H_Upper', 'image')
    S_t_select_Upper = cv.getTrackbarPos('S_Upper', 'image')
    V_t_select_Upper = cv.getTrackbarPos('V_Upper', 'image')
    #  Get current positions of 3 Track bars Lower thresh Values
    H_t_select_Lower = cv.getTrackbarPos('H_Lower', 'image')
    S_t_select_Lower = cv.getTrackbarPos('S_Lower', 'image')
    V_t_select_Lower = cv.getTrackbarPos('V_Lower', 'image')

    #  Set Limits for MASK
    frame_mask = cv.inRange(frame_HSV, (H_t_select_Lower, S_t_select_Lower, V_t_select_Lower),
                                 (H_t_select_Upper, S_t_select_Upper, V_t_select_Upper))

    """
    #  Set threshold limits
    ret, H_mat = cv.threshold(H, H_t_select_Lower, H_t_select_Upper, cv.THRESH_TRUNC)
    ret, S_mat = cv.threshold(S, S_t_select_Lower, S_t_select_Upper, cv.THRESH_TRUNC)
    ret, V_mat = cv.threshold(V, V_t_select_Lower, V_t_select_Upper, cv.THRESH_TRUNC)
    """

    kernel = np.ones((4, 4), np.uint8)
    mask = cv.morphologyEx(frame_mask, cv.MORPH_OPEN, kernel)   # CLEAN MASK NOISE
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)       # INCREASE MASK

    # Inverting mask(This shouldn't be here, for testing purposes only
    # mask = cv.bitwise_not(mask)

    frame = cv.bitwise_and(blur, blur, mask=mask)
    B, G, R = cv.split(frame)

    plt.clf()

    histB = cv.calcHist([B], [0], None, [256], [0, 256])
    histG = cv.calcHist([G], [0], None, [256], [0, 256])
    histR = cv.calcHist([R], [0], None, [256], [0, 256])

    plt.plot(histB, color='b')
    plt.plot(histG, color='g')
    plt.plot(histR, color='r')

    fig.canvas.draw()

    # HSV_IMAGE = cv.merge([H_mat, S_mat, V_mat])
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
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
FIELD_UPPER = np.array([180, 101, 237])
FIELD_LOWER = np.array([007, 000, 167])

 PLAYERS
RED
RED_UPPER = np.array([011, 255, 255])
RED_LOWER = np.array([000, 087, 092])

BLUE
BLUE_UPPER = np.array([102, 224, 255])
BLUE_LOWER = np.array([086, 125, 075])
"""
