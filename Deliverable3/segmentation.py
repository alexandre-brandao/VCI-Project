import cv2 as cv
import numpy as np

# global variables
mouseB = 77
mouseG = 127
mouseR = 53

# mouse click / toggle function
def toggle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global mouseB
        global mouseG
        global mouseR
        mouseB = frame[y,x,0]
        mouseG = frame[y,x,1]
        mouseR = frame[y,x,2]
        # arrayBGR = frame[y,x]
        print("CLICK!")


def nothing(x):
    pass

# video capture
cap = cv.VideoCapture('cambada.mp4')
cv.namedWindow('video')
cv.namedWindow('settings')
cv.namedWindow('result')
vidw = 768
vidh = 432
# recw = cap.get(3)
# rech = cap.get(4)

# trackbars
cv.createTrackbar('normal|HSV|YUV','settings',0,2,nothing)

cv.createTrackbar('1st frame: BLUE','settings',255,255,nothing)
cv.createTrackbar('1st frame: GREEN','settings',255,255,nothing)
cv.createTrackbar('1st frame: RED','settings',255,255,nothing)

cv.createTrackbar('2nd frame: BLUE','settings',255,255,nothing)
cv.createTrackbar('2nd frame: GREEN','settings',255,255,nothing)
cv.createTrackbar('2nd frame: RED','settings',255,255,nothing)

# variables
state = False

# mouse
cv.setMouseCallback('video',toggle)

# text information
font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 0.4
org = (5,15)
color = (0,0,0)
thickness = 1

while(True):
    ret, frame = cap.read()
    frame = cv.resize(frame, (768, 432))
    rate=cap.get(cv.CAP_PROP_FPS)
    pressKey = cv.waitKey(40)

    # color spaces
    rgb_frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    hsv_frame = cv.cvtColor(rgb_frame,cv.COLOR_BGR2HSV)

    # trackbar
    pallete = cv.getTrackbarPos('normal|HSV|YUV','settings')

    B1 = cv.getTrackbarPos('1st frame: BLUE','settings')
    G1 = cv.getTrackbarPos('1st frame: GREEN','settings')
    R1 = cv.getTrackbarPos('1st frame: RED','settings')

    B2 = cv.getTrackbarPos('2nd frame: BLUE','settings')
    G2 = cv.getTrackbarPos('2nd frame: GREEN','settings')
    R2 = cv.getTrackbarPos('2nd frame: RED','settings')

    # display color
    colordisp1 = np.zeros((100,300,3), np.uint8)
    colordisp1[:] = (mouseB,mouseG,mouseR)
    colordisp2 = np.zeros((100,300,3), np.uint8)
    colordisp2[:] = (B2, G2, R2)
    infodisp = "B = %d | G = %d | R = %d" % (mouseB, mouseG, mouseR)
    colordisp1 = cv.putText(colordisp1, infodisp, org, font,
                        fontScale, color, thickness, cv.LINE_AA)
    colordisp = np.concatenate((colordisp1,colordisp2),axis=1)

    # color segmentation
    color1 = (B1,G1,R1)
    color2 = (B2, G2, R2)
    mask = cv.inRange(hsv_frame, color1, color2)
    result1 = cv.bitwise_and(rgb_frame,rgb_frame,mask=mask)
    cv.imshow('result',result1)

    # pallete color visualization
    cv.imshow('settings',colordisp)

    if ret == False:
        break

    # display final frame
    if pallete == 1:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('video', frame)
    elif pallete == 2:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2YUV)

    cv.imshow('video', frame)

    # key to stop
    if pressKey == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
