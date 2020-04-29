import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass


img = cv.imread('messi5.jpg',0)
cv.namedWindow('THRESHOLD')
cv.createTrackbar('Upper', 'THRESHOLD', 255, 255, nothing)
cv.createTrackbar('Lower', 'THRESHOLD', 0, 255, nothing)

cap = cv.VideoCapture('CAMBADA.mp4')

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

    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame(stream end?). Exiting...")
        break

    upper = cv.getTrackbarPos('Upper', 'THRESHOLD')
    lower = cv.getTrackbarPos('Lower', 'THRESHOLD')
    edges = cv.Canny(img, lower, upper)

    cv.imshow('CannyEdges', edges)