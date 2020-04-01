import numpy as np
import cv2 as cv


def nothing(x):
    pass

img1 = cv.imread("p1.jpg")
laplacian1 = cv.Laplacian(img1, cv.CV_8U)
laplacian2 = cv.Laplacian(img1,cv.CV_32F)

cv.namedWindow('Gradients', cv.WINDOW_NORMAL)
cv.namedWindow('Settings', cv.WINDOW_AUTOSIZE)
cv.resizeWindow('Gradients',1280, 720)

tbname = 'Laplacian | Sobel (x/y) | Sobel (x&y)| Scharr (x&y)'
cv.createTrackbar(tbname,'Settings',0, 3, nothing)
cv.createTrackbar('depth (8U or 32F)','Settings',0,1,nothing)
cv.createTrackbar('xy', 'Settings', 0, 1, nothing)
cv.createTrackbar('kernel', 'Settings', 0, 60, nothing)

while(1):
    case = cv.getTrackbarPos(tbname, 'Settings')
    depth = cv.getTrackbarPos('depth (8U or 32F)','Settings')
    xy = cv.getTrackbarPos('xy', 'Settings')
    kernel = cv.getTrackbarPos('kernel', 'Settings')

    if case == 0:
        if depth==0:
            cv.imshow('Gradients', laplacian1)
        else:
            cv.imshow('Gradients', laplacian2)
    elif case == 1:
        if xy==0:
            if kernel==0 or kernel%2!=0: sobelx = cv.Sobel(img1,cv.CV_8U,1,0,ksize=kernel)
            cv.imshow('Gradients', sobelx)
        else:
            if kernel==0 or kernel%2!=0: sobely = cv.Sobel(img1,cv.CV_8U,0,1,ksize=kernel)
            cv.imshow('Gradients', sobely)
    elif case == 2:
        if kernel==0 or kernel%2!=0:
            sobelx = cv.Sobel(img1,cv.CV_8U,1,0,ksize=kernel) # eixo x
            sobely = cv.Sobel(img1,cv.CV_8U,0,1,ksize=kernel) # eixo y
            abs_sobelx = cv.convertScaleAbs(sobelx)
            abs_sobely = cv.convertScaleAbs(sobely)
            sobel = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0) # distribuir peso igual das 2 componentes
            cv.imshow('Gradients', sobel)
    else:
            scharrx= cv.Scharr(img1,cv.CV_8U,1,0,-1,kernel/30,cv.BORDER_DEFAULT)
            scharry = cv.Scharr(img1,cv.CV_8U,0,1,-1,kernel/30,cv.BORDER_DEFAULT)
            abs_scharrx = cv.convertScaleAbs(scharrx)
            abs_scharry = cv.convertScaleAbs(scharry)
            scharr = cv.addWeighted(abs_scharrx, 0.5, abs_scharry, 0.5, 0) # distribuir peso igual das 2 componentes
            cv.imshow('Gradients', scharr)

    k = cv.waitKey(1)
    if k==ord('q'): break

cv.destroyAllWindows()
