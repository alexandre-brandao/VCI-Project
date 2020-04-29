import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture('CAMBADA.mp4')

plt.ion()
fig = plt.figure()
plt.ylabel('Count')
plt.xlabel('Bins')
plt.xlim([0, 256])
plt.show()

while cap.isOpened():

    ret, frame = cap.read()
    frame = cv.resize(frame, (640, 480), interpolation=cv.INTER_AREA)
    #Color Space
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #frame = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
    resolution = 1080*1920
    #plt.clf()
    cv.imshow('Video', frame)
    if not ret:
        print('Frame Ended/No stream?')
        break

    color = ('b', 'g', 'r')
    #color = ('k')
    plt.clf()
    for i, col in enumerate(color):
        histr = cv.calcHist([frame], [i], None, [256], [0, 256])/resolution
        plt.plot(histr, color=col)



    fig.canvas.draw()

    if cv.waitKey(1) == ord('q'):
        print('Canceled')
        break

cap.release()
cv.destroyAllWindows()
