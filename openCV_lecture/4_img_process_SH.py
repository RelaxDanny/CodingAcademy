import cv2
import numpy as np 
import matplotlib.pylab as plt

img = cv2.imread("0_high.jpg")

#ROI -> Region of Interest 

x = 320; y = 150; w = 50; h = 50
roi = img[y:y+h, x:x+w]

print(roi.shape) #(50, 50, 3)

cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Thresholding !!! opencv top 3 valuable topic
"""
Grayscale Or Binary Image로 표현하는 이유는 이미지에서 원하는 피사체의 모양을 좀 더 정확하게 판단하기 위함이다.
종이위의 글씨 분리, 배경에서 전경을 분리 .. 등등의 작업

Thresholinding이란, 여러 점수들(pixel 값)을 커트라인을 정한 후 합격과 불합격으로 나눈다. 
여러 값을 경계점을 기준으로 두 가지 분류로 나누는 것으로, 바이너리 이미지를 만드는 가장 대표적인 방법이다.

binary img의 원리 : 컬러 이미지의 각 픽셀값이 특정 경계값을 넘으면 255, 못넘으면 0으로 설정 하는 작업.
"""
img = cv2.imread('newspaper.jpg', cv2.IMREAD_GRAYSCALE)

#NUmpy를 이용하여 binary img 만들기
thresh_np = np.zeros_like(img)
thresh_np[img>127] = 255

#opencv로 바이너리 이미지 만들기
ret, thresh_cv = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)

imgs = {'org': img, 'numpy': thresh_np, 'cv': thresh_cv}
for i, (key,value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([])
    plt.yticks([])
plt.show()