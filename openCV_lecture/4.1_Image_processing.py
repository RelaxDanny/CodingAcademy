#관심영역 지정
import cv
import numpy as np

img = cv2.imread('0_high.jpg')

#ROI = region of interest

x = 320; y = 150; w = 50; h = 50 #roi 좌표
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#관심영역 복제 및 새 창 띄우기
x = 320; y = 150; w = 50; h = 50 #roi 좌표
roi = img[y:y+h, x:x+w]
img2 = roi.copy() #numpy copy

img[y:y+h, x+w:x+w+w] = roi 
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0))
cv2.imshow("img", img)
cv2.imshow("roi", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

