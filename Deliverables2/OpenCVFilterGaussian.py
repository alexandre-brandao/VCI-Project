import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('maxresdefault.jpg')

blur = cv.GaussianBlur(img,(5,5),0)   # guassian BLUR


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()


while(cv.waitKey(1) != 'q'):
    pass

cv.destroyAllWindows()