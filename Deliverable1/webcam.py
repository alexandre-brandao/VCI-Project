import numpy as np
import cv2 as cv


def nothing(x):
    pass


# VideoCapture parameters
cap = cv.VideoCapture(0)

cv.namedWindow("frame")
cv.namedWindow("color")
cv.createTrackbar("Brightness", "frame", 500, 1000, nothing)
cv.createTrackbar("Contraste", "frame", 60, 500, nothing)
cv.createTrackbar("color/gray", "frame", 0, 1, nothing)

cv.createTrackbar("OFF/ON", "color", 0, 1, nothing)
cv.createTrackbar("red1_i", "color", 0, 255, nothing)
cv.createTrackbar("red2_i", "color", 50, 255, nothing)
cv.createTrackbar("red3_i", "color", 50, 255, nothing)
cv.createTrackbar("red1_f", "color", 10, 255, nothing)
cv.createTrackbar("red2_f", "color", 255, 255, nothing)
cv.createTrackbar("red3_f", "color", 255, 255, nothing)

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

    s = cv.getTrackbarPos("OFF/ON", "color")
    red1_i = cv.getTrackbarPos("red1_i", "color")
    red2_i = cv.getTrackbarPos("red2_i", "color")
    red3_i = cv.getTrackbarPos("red3_i", "color")
    red1_f = cv.getTrackbarPos("red1_f", "color")
    red2_f = cv.getTrackbarPos("red2_f", "color")
    red3_f = cv.getTrackbarPos("red3_f", "color")

    if color == 0:
        pass
    else:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # manipulating values
    frame_t = np.zeros(frame.shape, frame.dtype)
    frame = cv.addWeighted(frame, alpha/10-5, frame_t, 0, beta/2-250)

    # red color range
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_red = np.array([red1_i,red2_i,red3_i])
    upper_red = np.array([red1_f,red2_f,red3_f])
    mask_r = cv.inRange(hsv, lower_red, upper_red)
    red_only = cv.bitwise_and(frame, frame, mask=mask_r)
    mask = cv.cvtColor(mask_r, cv.COLOR_GRAY2BGR)
    res = cv.subtract(frame, mask)

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
    if s == 1:
        #cv.imshow("mask", mask)
        cv.imshow("frame", red_only)

    # key to stop
    if pressKey == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
