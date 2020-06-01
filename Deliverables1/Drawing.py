import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#Create a black image
img = np.zeros((512,512, 3), np.uint8)

# Drawing a diagonal blue line with thickness of 5 pixels
#img = cv.line(var, start, finish, color, thickness)
img = cv.line(img, (0,0), (511,511), (255,0,0), 5)

#Drawing rectangle
#img = cv.rectangle(img, top left, bottom right, color, thickness)
img = cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Drawing a circle#img = cv.circle(img, center, radius, color, -1)
img = cv.circle(img,(447,63), 63, (0,0,255), -1)

# Drawing an ellipse
img = cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#Drawing a Polygon
#insert array with vertice coordinates
pts = np.array([[10,5],[20,30],[70,20],[50, 10]], np.int32)
pts = pts.reshape((-1,1,2)) # seen as Z,x,y
img = cv.polylines(img,[pts], True, (0, 255, 255))

#Lets add text this to an image
""" To put texts in images, you need specify following things.
. Text data that you want to write
. Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
. Font type (Check cv2.putText() docs for supported fonts)
. Font Scale (specifies the size of font)
regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended"""

font = cv.FONT_ITALIC
var = str(123456789)
cv.putText(img, 'Alexandre Pereira', (5, 505), font, 0.8, (255, 255, 255), lineType=16)
cv.putText(img, 'Jose      Brandao', (5, 485), font, 0.6, (255, 255, 255), lineType=16)
cv.putText(img, 'Celso     Reis   ', (5, 465), font, 0.5, (255, 255, 255), lineType=16)
cv.putText(img, '00'+str(123456789), (5, 445), font, 0.4, (255, 255, 255), lineType=16)
cv.imshow('frame', img)

#Now put addimg on top of img, bottom left corner dim = (100,150)
addimg = cv.imread('panda.jpg')
Scale_Percentage = 30
width = int(addimg.shape[0] * Scale_Percentage / 100)
height = int(addimg.shape[1] * Scale_Percentage / 100)
dim = (width, height)
newimg = cv.resize(addimg, dim, interpolation=cv.INTER_AREA)

"""
#insert the image
img[img.shape[0]-newimg.shape[0]:img.shape[0], img.shape[1]-newimg.shape[1]:img.shape[1], :] = newimg
cv.imshow('frame with picture', img)
"""

#WATERMARK IMAGE
img[img.shape[0]-newimg.shape[0]:img.shape[0], img.shape[1]-newimg.shape[1]:img.shape[1], :] = img[img.shape[0]-newimg.shape[0]:img.shape[0], img.shape[1]-newimg.shape[1]:img.shape[1], :] + newimg*0.3
cv.imshow('frame with picture', img)

while cv.waitKey(1) != ord('q'):
    pass
cv.destroyAllWindows()
plt.hist(np.resize(newimg, (1, img.shape[0]*img.shape[1])),bins=256)
