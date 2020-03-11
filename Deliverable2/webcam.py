import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import argparse

def nothing(x):
    pass


# VideoCapture parameters
cap = cv.VideoCapture(0)
cv.namedWindow("frame")
cv.namedWindow("color")
cv.namedWindow("kernel")
cameraWidth = 640
cameraHeight = 480
cap.set(3,cameraWidth)
cap.set(4,cameraHeight)

# Trackbar
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

cv.createTrackbar("equalize", "kernel", 0, 1, nothing)
cv.createTrackbar("yuv", "kernel", 0, 1, nothing)
cv.createTrackbar("hsv", "kernel", 0, 1, nothing)
cv.createTrackbar("gaussian", "kernel", 0, 30, nothing)
cv.createTrackbar("blur", "kernel", 0, 50, nothing)

# Recording parameters
pause = False
record = False
fps = 24
rec_w = 1024
rec_h = 1024
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('resultado.avi', fourcc, fps, (640, 480))


# Parse parameters
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--color', type=str, default='rgb',
    help='Color space: "rgb" (default) or gray')
parser.add_argument('-b', '--bins', type=int, default=16,
    help='Number of bins per channel (default 16)')
parser.add_argument('-w', '--width', type=int, default=0,
    help='Resize video to specified width in pixels (maintains aspect)')
args = vars(parser.parse_args())

# Function arguments
color = args['color']
bins = args['bins']
resizeWidth = args['width']

# Initiliaze plot
fig, ax = plt.subplots()
ax.set_title('Histogram')
ax.set_xlabel('Bin')
ax.set_ylabel('Frequency')

# Initialize plot line objects + Interactive plotting
lw = 3
alpha = 0.5
lineR, = ax.plot(np.arange(bins), np.zeros((bins,)), c='r', lw=lw, alpha=alpha)
lineG, = ax.plot(np.arange(bins), np.zeros((bins,)), c='g', lw=lw, alpha=alpha)
lineB, = ax.plot(np.arange(bins), np.zeros((bins,)), c='b', lw=lw, alpha=alpha)
lineGray, = ax.plot(np.arange(bins), np.zeros((bins,1)), c='k', lw=lw)
ax.set_xlim(0, bins-1)
ax.set_ylim(0, 1)
plt.ion()
plt.show()

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

    noise_a = np.random.normal(0,0.7,frame.size)
    noise_a = noise_a.reshape(frame.shape[0], frame.shape[1], frame.shape[2]).astype('uint8')
    frame = cv.add(frame, noise_a)

    if ret == True:

        if resizeWidth > 0:
            (height, width) = frame.shape[:2]
            resizeHeight = int(float(resizeWidth/width)*height)
            frame = cv.resize(frame, (resizeWidth, resizeHeight),
                interpolation=cv.INTER_AREA)

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
        bw = cv.getTrackbarPos("color/gray", "frame")

        s = cv.getTrackbarPos("OFF/ON", "color")
        red1_i = cv.getTrackbarPos("red1_i", "color")
        red2_i = cv.getTrackbarPos("red2_i", "color")
        red3_i = cv.getTrackbarPos("red3_i", "color")
        red1_f = cv.getTrackbarPos("red1_f", "color")
        red2_f = cv.getTrackbarPos("red2_f", "color")
        red3_f = cv.getTrackbarPos("red3_f", "color")

        a_equ = cv.getTrackbarPos("equalize","kernel")
        a_yuv = cv.getTrackbarPos("yuv","kernel")
        a_hsv = cv.getTrackbarPos("hsv","kernel")
        blur = cv.getTrackbarPos("blur","kernel")
        gaus = cv.getTrackbarPos("gaussian","kernel")

        if bw == 1:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            if a_equ == 1:
                equ = cv.equalizeHist(frame)
                frame = np.hstack((frame,equ))

        elif s == 1:
            #cv.imshow("mask", mask)
            cv.imshow("frame", red_only)
        elif a_hsv == 1:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        elif a_yuv == 1:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2YUV)

        if blur > 0:
            frame = cv.blur(frame,(blur+1,blur+1))

        if (gaus > 0) and (gaus % 2 == 0):
            frame = cv.medianBlur(frame,gaus+1)

        # color range
        if bw == 0:
            # manipulating values
            frame_t = np.zeros(frame.shape, frame.dtype)
            frame = cv.addWeighted(frame, alpha/10-5, frame_t, 0, beta/2-250)

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

        # display the histogram
        numPixels = np.prod(frame.shape[:2])
        if bw == 0:
            (b, g, r) = cv.split(frame)
            histogramR = cv.calcHist([r], [0], None, [bins], [0, 255]) / numPixels
            histogramG = cv.calcHist([g], [0], None, [bins], [0, 255]) / numPixels
            histogramB = cv.calcHist([b], [0], None, [bins], [0, 255]) / numPixels
            lineR.set_ydata(histogramR)
            lineG.set_ydata(histogramG)
            lineB.set_ydata(histogramB)
            lineGray.set_ydata(0)
        else:
            histogram = cv.calcHist([frame], [0], None, [bins], [0, 255]) / numPixels
            lineGray.set_ydata(histogram)
            lineR.set_ydata(0)
            lineG.set_ydata(0)
            lineB.set_ydata(0)
        fig.canvas.draw()

        # key to stop
        if pressKey == ord('q'):
            break


cap.release()
cv.destroyAllWindows()
