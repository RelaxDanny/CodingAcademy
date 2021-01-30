import numpy as np
import cv2 as cv

img = cv.imread('img/white_cab.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,800,500)
#x, y, w, h

cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

img = img*mask2[:,:,np.newaxis]


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()

plt.imshow(img),plt.colorbar(),plt.show()

