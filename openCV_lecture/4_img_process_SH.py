import cv2
import numpy as np 
import matplotlib.pylab as plt

# img = cv2.imread("0_high.jpg")

# #ROI -> Region of Interest 

# x = 320; y = 150; w = 50; h = 50
# roi = img[y:y+h, x:x+w]

# print(roi.shape) #(50, 50, 3)

# cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #Thresholding !!! opencv top 3 valuable topic
# """
# Grayscale Or Binary Image로 표현하는 이유는 이미지에서 원하는 피사체의 모양을 좀 더 정확하게 판단하기 위함이다.
# 종이위의 글씨 분리, 배경에서 전경을 분리 .. 등등의 작업

# Thresholinding이란, 여러 점수들(pixel 값)을 커트라인을 정한 후 합격과 불합격으로 나눈다. 
# 여러 값을 경계점을 기준으로 두 가지 분류로 나누는 것으로, 바이너리 이미지를 만드는 가장 대표적인 방법이다.

# binary img의 원리 : 컬러 이미지의 각 픽셀값이 특정 경계값을 넘으면 255, 못넘으면 0으로 설정 하는 작업.
# """
# img = cv2.imread('newspaper.jpg', cv2.IMREAD_GRAYSCALE)

# #NUmpy를 이용하여 binary img 만들기
# thresh_np = np.zeros_like(img)
# thresh_np[img>127] = 255

#opencv로 바이너리 이미지 만들기
# ret, thresh_cv = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY)

# imgs = {'org': img, 'numpy': thresh_np, 'cv': thresh_cv}
# for i, (key,value) in enumerate(imgs.items()):
#     plt.subplot(1, 3, i+1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([])
# # plt.show()

# img = cv2.imread('img/0_high.jpg', cv2.IMREAD_GRAYSCALE)

# #경계 값을 130으로 지정해줄거임
# _, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)

# #경계 값을 지정하지 않고 OTSU 알고리즘을 사용한 결과 값
# t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print('Otsu Threshold: ', t)

# imgs = {'original': img, 't130': t_130, 'otsu:': t_otsu}

# for i, (k, v) in enumerate(imgs.items()):
#     plt.subplot(1,3,i+1)
#     plt.title(k)
#     plt.imshow(v, cmap='gray')
#     plt.xticks([]); plt.yticks([])

# plt.show()

#적응형 스레시홀드 적용법

# blk_size = 9
# C = 5
# img = cv2.imread('img/test2.png', cv2.IMREAD_GRAYSCALE)

# #오츠의 알고리즘으로 단일경계 값을 전체 이미지에 적용 불완전 알고리즘
# ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# #어뎁티브 스레시홀드를 평균과 가우시안 분포로 각각 적용
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

# imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, \
#         'Adapted-Mean':th2, 'Adapted-Gaussian': th3}
# for i, (k, v) in enumerate(imgs.items()):
#     plt.subplot(2,2,i+1)
#     plt.title(k)
#     plt.imshow(v,'gray')
#     plt.xticks([]),plt.yticks([])

# plt.show()

#이미지 합성!
import cv2
import numpy as np
import matplotlib.pylab as plt 

img1 = cv2.imread('img/0_high.jpg')
img2 = cv2.imread('img/sudoku.png')

# #두 사진의 픽셀 덧셈
# img3 = img1 + img2 # 화소가 고르지 못하고 중간 이미지 색이 이상해짐
# img4 = cv2.add(img1, img2) #하얀 픽셀들이 엄청나옴 

# imgs = {"img1" : img1, "img2" : img2, "img3" : img3, "img4" : img4}

# for i, (k,v) in enumerate(imgs.items()):
#     plt.subplot(2,2,i+1)
#     plt.imshow(v[:,:,::-1])
#     plt.title("test")
#     plt.xticks([]); plt.yticks([])
# plt.show()

#Alpha blending

# alpha = 0.5 # 50%
# blended = img1 * alpha + img2 *(1-alpha)
# cv2.imshow("blended", blended)

# #add weighted() 알파블랜딩 적용
# res = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
# cv2.imshow('cv2.addweighted', res)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Track bar을 이용해서 알파블렌딩 설정하기

win_name = "Alpha belnding"
trackbar_name = "fade"

#트랙바 이벤트 핸들러 함수
def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    cv2.imshow(win_name, dst)

img1 = cv2.imread('img/man_face.jpg')
img2 = cv2.imread("img/lion_face.jpg")

cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()



