import numpy as np
import cv2 as cv

def nothing(x):
    pass

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv.Canny(image, lower, upper)
	# return the edged image
	return edged


img1 = cv.imread("p1.jpg")

hsv = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv, (59, 9, 89), (89,187,255))
imask = mask>0
green = np.zeros_like(img1, np.uint8)
green[imask] = img1[imask]


cv.namedWindow('Image', cv.WINDOW_NORMAL)
cv.resizeWindow('Image', 1280,720)
cv.namedWindow('Settings')
cv.createTrackbar('Algorithm', 'Settings', 0, 1, nothing)
cv.createTrackbar('threshold (3:1)', 'Settings', 0, 500, nothing)

while(1):
    alg = cv.getTrackbarPos('Algorithm', 'Settings')
    thr = cv.getTrackbarPos('threshold (3:1)', 'Settings')

    if alg == 0:
        edges = cv.Canny(green,3*thr,thr)
        edges = cv.GaussianBlur(edges, (5,5), 0)
    elif alg == 1: 
        edges = auto_canny(img1, 0.1)
        edges = cv.GaussianBlur(edges, (5, 5), 0)
    
    cv.imshow('Image',edges)

    k = cv.waitKey(1);
    if k == ord('q'): break

cv.destroyAllWindows()

