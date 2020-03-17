import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
    pass

clear = False;

# Initial analysis
img1 = cv.imread('CAMBADA_CLOSEUP.png')
img1 = cv.resize(img1, (1366, 768), interpolation=cv.INTER_AREA)
img = cv.GaussianBlur(img1,(5,5),0)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Track bar window and settinf
cv.namedWindow('THRESHOLD')
cv.createTrackbar('Binary:', 'THRESHOLD', 127, 255, nothing)
switch = '0 : SET BINARY LIM \n 1 : CHOOSING CONTOURS'
cv.createTrackbar(switch, 'THRESHOLD', 0, 1, nothing)
cv.createTrackbar(switch, 'THRESHOLD', 0,20, nothing)


while 1:
    # Get Trackbar values

    s = cv.getTrackbarPos(switch, 'THRESHOLD')
    thres = cv.getTrackbarPos('Binary:', 'THRESHOLD')


    if(s == 0):
        if(clear == True):
            cv.destroyWindow('THRESHOLD')
            cv.namedWindow('THRESHOLD')
            cv.createTrackbar('Binary:', 'THRESHOLD', thres, 255, nothing)
            cv.createTrackbar(switch, 'THRESHOLD', 0, 1, nothing)

        _, binary = cv.threshold(img, thres, 255, 0)
        ## Countors is used to draw lines over a boundary or boundaries with the intensity
        kernel = np.ones((4, 4), np.uint8)
        binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=5)  # CLEAN MASK NOISE
        clear = False

        contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        lenc = len(contours)
        print("Number of countours: " + str(lenc))

        img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img1 = cv.drawContours(img1, contours, -1, (0, 255, 255), 3)
        cv.imshow('countored image', img1)

    if(s==1):
        # Set new trackbars
        if(clear == False):
            clear = True
            cv.destroyWindow('THRESHOLD')
            cv.namedWindow('THRESHOLD')
            cv.createTrackbar(switch, 'THRESHOLD', 1, 1, nothing)
            cv.createTrackbar('Contour(idx)', 'THRESHOLD', 0, lenc-1, nothing)

        contouridx = cv.getTrackbarPos('Contour(idx)', 'THRESHOLD')

        img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img1 = cv.drawContours(img1, contours[contouridx], -1, (0, 125, 255), 3)
        cv.imshow('choose image', img1)

    """https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features"""

    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
