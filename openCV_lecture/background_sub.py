# import numpy as np
# import cv2 as cv

# img = cv.imread('0_high.jpg')

# mask = np.zeros(img.shape[:2],np.uint8)
# bgdModel = np.zeros((1,65),np.float64)
# fgdModel = np.zeros((1,65),np.float64)

# rect = (50,50,500,500)

# cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

# mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

# img = img*mask2[:,:,np.newaxis]

# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# # plt.imshow(img),plt.colorbar(),plt.show()

# I am new to opencv-python. I have found the lines in image through houghtransformP. The lines drawn from hough transform are discontinued and are giving multiple lines. I need to draw only one line for the edges and find the 'distance' between lines which are found.

# The output image is shown below

# """
# Created on Fri Nov  8 11:41:16 2019

# @author: romanth.chowan
# """
import cv2
import numpy as np
import matplotlib
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

img = cv2.imread('0_high_sub.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

low_threshold = 0
high_threshold = 200
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 15  # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50  # minimum number of pixels making up a line
max_line_gap = 20  # maximum gap in pixels between connectable line segments
line_image = np.copy(img) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                    min_line_length, max_line_gap)

for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

# Draw the lines on the  image
lines_edges = cv2.addWeighted(img, 0.8, line_image, 1, 0)
cv2.imshow('img', lines_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()