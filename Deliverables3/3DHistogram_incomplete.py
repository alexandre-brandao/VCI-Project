import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('construcsite.jpg')



plt.ylabel('Count')
plt.xlabel('Bins')
plt.xlim([0, 256])


#Color Space
#frame = cv.cvtColor(img, cv.COLOR_BGR2GRAy)

hsv_frame = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv_frame)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3D')
hist, xo, yo = np.histogram2d(h, s, bins=[256, range=[[0, 255],[0, 255]])

resolution = 450*280

print(h)

color = ('V', 'S', 'H')
#color = ('k')

for i, col in enumerate(color):
    pass


#fig.canvas.draw()

while cv.waitKey(1) != ord('q'):
    pass


print('Canceled')
cv.destroyAllWindows()
