import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('maxresdefault.jpg')
noise = np.zeros((738,1568,3), 'uint8')

noise = cv.randn(noise, 0, 5) #mean and noise
kernel = np.ones((5, 5), np.float32)/25   # 5*5 array composing => 1/25 is the weight of each element
img = img + noise
dst = cv.bilateralFilter(img,9,500,500)

plt.subplot(121),plt.imshow(img),plt.title('Original+noise')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Bilateral Filter')
plt.xticks([]), plt.yticks([])
plt.show()


while(cv.waitKey(1) != 'q'):
    pass

cv.destroyAllWindows()