import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

cap = cv.VideoCapture('CAMBADA.mp4')


cv.namedWindow('THRESHOLD')

cv.createTrackbar('UPPER', 'THRESHOLD', 255, 255, nothing)
cv.createTrackbar('LOWER', 'THRESHOLD', 0, 255, nothing)

cv.createTrackbar('MAX_LINE_GAP', 'THRESHOLD', 255, 255, nothing)
cv.createTrackbar('MIN_LINE_LENGTH', 'THRESHOLD', 0, 255, nothing)


if not cap.isOpened():
        print("Cannot open camera")


while True:

    # Key INPUT
    k = cv.waitKey(1) & 0xFF
    if(k == 27):
        break

    #Capture frame-by-frame
    ret, img = cap.read()
    img = cv.GaussianBlur(img, (5, 5), 0)
    img1= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame(stream end?). Exiting...")
        break

    upper = cv.getTrackbarPos('UPPER', 'THRESHOLD')
    lower = cv.getTrackbarPos('LOWER', 'THRESHOLD')

    MLG = cv.getTrackbarPos('MAX_LINE_GAP', 'THRESHOLD')
    MLL = cv.getTrackbarPos('MIN_LINE_LENGTH', 'THRESHOLD')

    edges = cv.Canny(img1, lower, upper)


    # Recommend minLineLength = 003, max LineGap = 49 for upper = 178, lower=59
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 50, None, minLineLength=MLL, maxLineGap=MLG)
    # Draw lines on the image

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)


    # Apply hough transform on the image
    circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, img.shape[0] / 64, param1=200, param2=10, minRadius=5, maxRadius=30)
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
