import numpy as np
import cv2 as cv

img = cv.imread('img/white_cab.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,800,500)

cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

img = img*mask2[:,:,np.newaxis]

# print(np.where(img>250, 0, img)) #보다 크면 1로, 아닐경우 0으로
# img = np.where(img == 0, 255, img)
# print(a)
# lower = np.array([200,255,255])
# upper = np.array([255,255,255])

# mask = cv.inRange(hsv, lower, upper)
# img[mask>0] = (0,0,100)
# print(np.where(a>15, 99, a)) #아닐경우 그대로
# print(np.where(a>15, a, 0)) #아닐경우 0으로
# print(a)



cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()

plt.imshow(img),plt.colorbar(),plt.show()


# #++++++++++++++++++++++++++++++++++++++++++++++++++++
# import cv2
# import numpy as np
# import matplotlib
# from matplotlib.pyplot import imshow
# from matplotlib import pyplot as plt

# img = cv2.imread('img/white_cab.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# kernel_size = 5
# blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# low_threshold = 0
# high_threshold = 200
# edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# rho = 1  # distance resolution in pixels of the Hough grid
# theta = np.pi / 180  # angular resolution in radians of the Hough grid
# threshold = 100  # minimum number of votes (intersections in Hough grid cell)
# min_line_length = 100  # minimum number of pixels making up a line
# max_line_gap = 20  # maximum gap in pixels between connectable line segments
# line_image = np.copy(img) * 0  # creating a blank to draw lines on

# # Run Hough on edge detected image
# # Output "lines" is an array containing endpoints of detected line segments
# lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
#                     min_line_length, max_line_gap)

# for line in lines:
#     for x1,y1,x2,y2 in line:
#         cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

# # Draw the lines on the  image
# lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
# cv2.imshow('img', lines_edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()