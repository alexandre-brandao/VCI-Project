import numpy as np
import cv2 as cv


def nothing(x):
    pass


# VideoCapture parameters
cap = cv.VideoCapture(0)

cv.namedWindow("frame")
cv.createTrackbar("Brightness", "frame", 500, 1000, nothing)
cv.createTrackbar("Contraste", "frame", 6, 50, nothing)
cv.createTrackbar("color/gray", "frame", 0, 1, nothing)

# Recording parameters
pause = False
record = False
fps = 24
rec_w = 1024
rec_h = 1024
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('resultado.avi', fourcc, fps, (640, 480))

# Watermark parameters
text1 = "Visao Por Computador na Industria (UA)"
text2 = "g: gravar | p: pausar | s: parar | q: quit"
status = "        "

font = cv.FONT_HERSHEY_PLAIN
rectangle_bgr = (255, 255, 255)
font_scale = 1


t1_x = 0
t1_y = 16
(w1, h1) = cv.getTextSize(text1, font, fontScale=font_scale, thickness=1)[0]
box1 = ((t1_x, t1_y), (t1_x + w1 + 2, t1_y - h1 - 2))

t2_x = 0
t2_y = 30
(w2, h2) = cv.getTextSize(text2, font, fontScale=font_scale, thickness=1)[0]
box2 = ((t2_x, t2_y + 2), (t2_x + w2 + 2, t2_y - h2 -2))

t3_x = 550
t3_y = 16
font_scale2 = 1
(w3, h3) = cv.getTextSize(status, font, fontScale=font_scale2, thickness=1)[0]
statusbox = ((t3_x, t3_y + 2), (t3_x + 20 + w3 + 2, t3_y - h3 -2))



# loop
while(True):
    # frame by frame
    ret, frame = cap.read()

    # watermark
    cv.rectangle(frame, box1[0], box1[1], rectangle_bgr, cv.FILLED)
    cv.putText(frame, text1, (t1_x, t1_y), font, 1, (0, 0, 0))
    cv.rectangle(frame, box2[0], box2[1], rectangle_bgr, cv.FILLED)
    cv.putText(frame, text2, (t2_x, t2_y), font, 1, (0, 0, 0))
    cv.rectangle(frame, statusbox[0], statusbox[1], rectangle_bgr, cv.FILLED)
    cv.putText(frame, status, (t3_x, t3_y), font, 1, (0, 0, 0))

    # trackbar
    beta = cv.getTrackbarPos("Brightness", "frame")
    alpha = cv.getTrackbarPos("Contraste", "frame")
    color = cv.getTrackbarPos("color/gray", "frame")

    if color == 0:
        pass
    else:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # manipulating values
    frame_t = np.zeros(frame.shape, frame.dtype)
    frame = cv.addWeighted(frame, alpha-5, frame_t, 0, beta/2-250)

    # recording
    pressKey = cv.waitKey(1)

    if record == True and pause == False:
        out.write(frame)
        status = "A GRAVAR"

    if pressKey == ord('g'):
        record = True
        status = "A GRAVAR"
    elif pressKey == ord('p') and record == True:
        if not pause:
            pause = True
            status = "PAUSADO"
        else:
            pause = False
    elif pressKey == ord('s'):
        pause = False
        record = False
        status = "GUARDADO"
        out.release()

    # display final frame
    cv.imshow("frame", frame)

    # key to stop
    if pressKey == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
