import matplotlib.pyplot as plt
import numpy as np

# # a = np.array([2,6,7,3,12,8,4,5])
# # plt.plot(a)
# # plt.show()

# # # 2. y=x^2 그래프 그리기
# # x = np.arange(10) 
# # # x = [0 1 2 3 4 5 6 7 8 9] * 2
# # # y = x numpy 의 제곱값
# # y = x**2
# # print(y)
# # plt.plot(x,y)

# # plt.show()

# x = np.arange(10)
# y = x**2
# """
# - : 실선 
# -. : 점 이음선
# . : 점
# o : 원
# ^ : 정삼각형
# > : 우 삼각형
# 2 : 작은 정삼각형
# 4 : 작은 우 삼각형
# p : 오각형
# h : 육각형
# D : 다이아몬드 표
# -- : 이음선
# : : 점선
# , : 픽셀
# v : 역삼각형
# < : 좌 삼각형
# 1 : 작은 역삼각형
# 3 : 작은 좌 삼각형
# s : 사각형
# * : 별표
# + : 더하기 표
# x : 엑스 표
# """
# x = np.arange(10)
# f1 = x + 5
# f2 = x **2
# f3 = x **2 + x*2

# plt.plot(x, 'r--')
# plt.plot(f1, 'g-')
# plt.plot(f2, 'bv')
# plt.plot(f3, 'ks')
# plt.show()


# # subplot
# x = np.arange(10)
# plt.subplot(2, 2, 1) #221 -> 2행 2열 중의 첫번째 사진 또는 그래프
# plt.plot(x, x**2)

# plt.subplot(2, 2, 2) #222 -> 2행 2열의 두번째 그래프
# plt.plot(x, x*5)

# plt.subplot(223)
# plt.plot(x, np.sin(x))

# plt.subplot(224)
# plt.plot(x, np.tan(x))

# plt.show()

import cv2
img = cv2.imread('0_high.jpg') # BGR [1,2,3]
plt.imshow(img[:, :, ::-1])
#img[:, :, :] 3차원의 모든 내용을 선택한다. 이때 마지막 측의 길이가 3이므로 다시 img[:, :, ::]로 바꿀수 있음
#이 때 마지막 축의 요소를 거꾸로 뒤집기 위해, img[:, :, ::-1] -> img[:, :, (2,1,0)] - > 0, 1, 2 -> BGR -> RGB
plt.xticks([])
plt.yticks([])
plt.show()