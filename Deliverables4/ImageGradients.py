import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


imgo = cv.imread('CAMBADAFIELD2.png')
imgo = cv.cvtColor(imgo, cv.COLOR_BGR2RGB)
# convert to grayscale
img = cv.cvtColor(imgo, cv.COLOR_RGB2GRAY)
img = cv.medianBlur(img, 5)
cv.imshow('Original', img)


laplacian = cv.Laplacian(img,cv.CV_64F)

sobelx = cv .Sobel(img,cv.CV_64F,1,0,ksize=5)
abs_sobelx = np.absolute(sobelx)
sobel_x = np.uint8(abs_sobelx)

sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
abs_sobely = np.absolute(sobely)
sobel_y = np.uint8(abs_sobely)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.colorbar()
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2),plt.imshow(laplacian,cmap='gray'), plt.colorbar()
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3),plt.imshow(sobelx,cmap='gray'), plt.colorbar()
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray'), plt.colorbar()
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()