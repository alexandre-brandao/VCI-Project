"""
    @author Alexandre Brandao
    Date    24/02/2020
    Overview:
        Video compression in OpenCV
        CODECS
        A “codec” is used to compress and decompress a video file
        A “container” is a collection of files that stores information about the digital file.
        - X264 gives very small size video
            Works with : .mp4 .avi
        - MJPG gives high resolution video
            Works with : .avi
        - XviD
        - H.264
        - DivX
            Works with : --
        - QPEG
            Works with : .avi
        - MPEG-4
            Works with : --
        - mp4v
            Works with :  --
        Note: List of codecs http://www.fourcc.org/codecs.php#letter_a
"""

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('CAMBADA.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 30.0, (1920,1080))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv.flip(frame, 0)
        # write the flipped frame
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        out.write(frame)

        cv.imshow('frame', frame)

        if(cv.waitKey(1) & 0xFF == ord('q')):
            break

    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
