import numpy as np
import cv2 as cv

#Import video
cap = cv.VideoCapture('CAMBADA.mp4');

#Read video frames...
if not cap.isOpened():
    print('Unable to load file')

while True:
    # Ret serves as a boolean to load
    # frame is the current image being analysed
    ret, frame = cap.read()

    if not ret:
        print('Stream end?...')
        break

    #Apply operations to the frames
    gray = cv.cvtColor(frame, cv.COLOR_RGB2Luv)

    #Show frame
    cv.imshow('frame', gray)

    # To force leave the stream
    # Wait 1 millisecond for key input
    if cv.waitKey(1) == ord('q'): #Ord converts char to its respected value
        break

#Release cap
cap.release()
#Destroy all Windows
cv.destroyAllWindows()
