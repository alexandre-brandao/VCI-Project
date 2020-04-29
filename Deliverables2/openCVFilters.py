import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('maxresdefault.jpg')

kernel = np.ones((5,5),np.float32)/25   # 5*5 array composing => 1/25 is the weight of each element
dst = cv.filter2D(img,-1, kernel)   # "-1" stands for the anchor center(Default Value)


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


while(cv.waitKey(1) != 'q'):
    pass

cv.destroyAllWindows()