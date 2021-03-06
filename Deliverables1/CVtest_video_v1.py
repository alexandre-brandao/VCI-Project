import numpy as np
import cv2 as cv

cap = cv.VideoCapture('../Deliverables4/CAMBADA.mp4')

if not cap.isOpened():
        print("Cannot open camera")

while True:
    #Capture frame-by-frame
    ret, frame = cap.read();

    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame(stream end?). Exiting...")
        break
    #Our operations on the frame come from here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
#When everything is done, release the Capture
cap.release()
cv.destroyAllWindows()
