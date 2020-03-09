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


img = cv.imread('CAMBADAFIELD.png')
img = cv.resize(img, (640, 480), interpolation=cv.INTER_AREA)
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
cv.createTrackbar('H_Upper', 'image', 255, 255, nothing)
cv.createTrackbar('S_Upper', 'image', 255, 255, nothing)
cv.createTrackbar('V_Upper', 'image', 255, 255, nothing)
cv.createTrackbar('H_Lower', 'image', 0, 255, nothing)
cv.createTrackbar('S_Lower', 'image', 0, 255, nothing)
cv.createTrackbar('V_Lower', 'image', 0, 255, nothing)

# create switch for ON | OFF functionality
cv.setMouseCallback('image', paint)

#  Obtain HSV values from image
H, S, V = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))

while 1:
    print("Hello")
    k = cv.waitKey(1) & 0xFF

    #  Get current positions of 3 Track bars Upper thresh Values
    H_t_select_Upper = cv.getTrackbarPos('H_Upper', 'image')
    S_t_select_Upper = cv.getTrackbarPos('S_Upper', 'image')
    V_t_select_Upper = cv.getTrackbarPos('V_Upper', 'image')
    #  Get current positions of 3 Track bars Lower thresh Values
    H_t_select_Lower = cv.getTrackbarPos('H_Lower', 'image')
    S_t_select_Lower = cv.getTrackbarPos('S_Lower', 'image')
    V_t_select_Lower = cv.getTrackbarPos('V_Lower', 'image')

    #  Set threshold limits

    ret, H_mat = cv.threshold(H, H_t_select_Lower, H_t_select_Upper, cv.THRESH_TOZERO)
    ret, S_mat = cv.threshold(S, S_t_select_Lower, S_t_select_Upper, cv.THRESH_TOZERO)
    ret, V_mat = cv.threshold(V, V_t_select_Lower, V_t_select_Upper, cv.THRESH_TOZERO)

    plt.clf()

    histH = cv.calcHist([H_mat], [0], None, [256], [0, 256])
    histS = cv.calcHist([S_mat], [0], None, [256], [0, 256])
    histV = cv.calcHist([V_mat], [0], None, [256], [0, 256])

    plt.plot(histH, color='R')
    plt.plot(histS, color='g')
    plt.plot(histV, color='k')

    fig.canvas.draw()

    HSV_IMAGE = cv.merge([H_mat, S_mat, V_mat])
    frame = cv.cvtColor(HSV_IMAGE, cv.COLOR_HSV2BGR)
    cv.imshow('image', frame)

    if regionSelected:
        pass

    if k == 27:
        break

