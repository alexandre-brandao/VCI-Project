# C:\Users\Celso Pereira\source\repos\PythonApplication1\PythonApplication1
#https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html

# An image gradient is a directional change in the intensity or color in an image
#https://www.youtube.com/watch?v=aDY4aBLFOIg&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=22&t=0s
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('robocup.jpg', cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img, cv.CV_64F, ksize=3)           # 64 bit float to suport negative numbers
laplacian = np.uint8(np.absolute(laplacian))

sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)            # Vertical change
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)            # Horizontal change
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelcombined = cv.bitwise_or(sobelx, sobely)               # Combine two results, bitwise operator

titles = ['Image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined']
images = [img, laplacian, sobelx, sobely, sobelcombined]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

'''
# Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.
# The Canny edge detection algorithm is composed of 5 steps:
#   1. Noise reduction
#   2. Gradient calculation
#   3. Non-maximum suppression
#   4. Double threshold
#   5. Edge Tracking by Hysteresis
#https://www.youtube.com/watch?v=CGfXCkHNemo&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=23&t=370s
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def changepar(x):
    pass

img = cv.imread('robocup.jpg', 0)

cv.namedWindow('background')
cv.createTrackbar('L', 'background', 0, 800, changepar)
cv.createTrackbar('H', 'background', 100, 800, changepar)

while(1):
    k = cv.waitKey(1) & 0xFF == ord("q")
    if k == 27:
        break

    l = cv.getTrackbarPos('L', 'background')
    h = cv.getTrackbarPos('H', 'background')

    canny = cv.Canny(img, l, h)                          # default = ApertureSize aperture size for the Sobel operator (apertureSize=3)

    titles = ['Image', 'Canny']
    images = [img, canny]

    for i in range(2):
        plt.subplot(1,2,i+1)
        plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()
'''
# Motion detection and Tracking using Opencv contours
#https://www.youtube.com/watch?v=MkcUgPhOlP8&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=29&t=58s
''''''

#Line detection and ball detection using the Hough transform
# https://www.youtube.com/watch?v=rVBVqVmHtfc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=35&t=0s
# https://www.youtube.com/watch?v=dp1r9oT_h9k&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=39&t=0s
'''
import  cv2 as cv
import numpy as np

 #We can also limitate the ROI

img = cv.imread('game1.jpg')
output = img.copy()

# Lines
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow('edges', edges)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    # Draw line
    cv.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

# Circle
gray1 = cv.medianBlur(gray, 5)
circles = cv.HoughCircles(gray1, cv.HOUGH_GRADIENT, 1, 350, param1=199, param2=51, minRadius=30, maxRadius=0)
detected_circles = np.uint16(np.around(circles))

for (x,y,r) in detected_circles[0,:]:
    # Draw the outer circle
    cv.circle(output, (x,y), r, (0,255,0), 3)
    # Draw the center of the circle
    cv.circle(output, (x,y), 2, (0,255,255), 3)

cv.imshow('image', img)
cv.imshow('output', output)
k = cv.waitKey(0)
cv.destroyAllWindows()

'''
# Template matching to detect the robots
#https://www.youtube.com/watch?v=sghglbXyjHc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=32&t=0s
#https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
# Could be improved!

'''
import cv2 as cv
import numpy as np

img = cv.imread('game1.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('player4.png', 0)

#To know w,h of the template
w,h = template.shape[::-1]

res = cv.matchTemplate(gray_img, template, cv.TM_CCOEFF_NORMED)         #Other methods TM_SQDIFF_NORMED, TM_CCORR_NORMED
print(res)
threshold = 0.71298;
loc = np.where(res >= threshold)
print(loc)

#If there are multiple number of matched templates
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
'''

############################### Machine Learning ##############################
# In a separate code!


# Camera calibration
# https://docs.opencv.org/4.2.0/dc/dbb/tutorial_py_calibration.html
# http://www.dmi.unict.it/~furnari/teaching/CV1617/lab1/
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html

# Two major distortions are radial distortion and tangential distortion.
# Due to radial distortion, straight lines will appear curved. Its effect is more as we move away from the center of image.
# Tangential distortion occurs because image taking lense is not aligned perfectly parallel to the imaging plane. So some areas in image may look nearer than expected.
# Intrinsic parameters are specific to a camera. It includes information like focal length (f_x,f_y), optical centers (c_x, c_y) etc.
#It is also called camera matrix. It depends on the camera only, so once calculated, it can be stored for future purposes. It is expressed as a 3x3 matrix.
# Extrinsic parameters corresponds to rotation and translation vectors which translates a coordinates of a 3D point to a coordinate system.
# To find all these parameters, what we have to do is to provide some sample images of a well defined pattern (eg, chess board).
#We find some specific points in it (square corners in chess board). We know its coordinates in real world space and we know its coordinates in image.
#With these data, some mathematical problem is solved in background to get the distortion coefficients.
# We need atleast 10 test patterns for camera calibration.

import numpy as np
import cv2
import glob
from numpy import load

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

img = cv2.imread('left12.jpg')
h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

## Method: Using cv2.undistort()
## undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)

tot_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    tot_error += error

print("total error: ", tot_error/len(objpoints))

# Store the camera matrix and distortion coefficients
np.savez('data.npz', cameramatrix=newcameramtx, distortion=dist)
data = load('data.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
