# 1. plt 그림 그리기 
import matplotlib.pyplot as plt
import numpy as np

a = np.array([2,6,7,3,12,8,4,5])
plt.plot(a)
plt.show()

# 2. y = x^2 그래프 그리기
x = np.arange(10) # 0,1,2,3,4,5,6,7,8,9
y = x **2
plt.plot(x,y)
plt.show()


# 3. plot의 색 지정
x = np.arange(10)
y = x **2
plt.plot(x,y, "r") # b, g, r, c(Cyan청록색), m(Magenta 자홍색), y(yellow), k(black), w(white)


# 4 다양한 스타일 지정
"""
- : 실선 
-. : 점 이음선
. : 점
o : 원
^ : 정삼각형
> : 우 삼각형
2 : 작은 정삼각형
4 : 작은 우 삼각형
p : 오각형
h : 육각형
D : 다이아몬드 표
-- : 이음선
: : 점선
, : 픽셀
v : 역삼각형
< : 좌 삼각형
1 : 작은 역삼각형
3 : 작은 좌 삼각형
s : 사각형
* : 별표
+ : 더하기 표
x : 엑스 표
"""
x = np.arange(10)
print(x + 5)
f1 = x + 5
f2 = x ** 2
f3 = x **2 + x*2

plt.plot(x, 'r--') #빨간색 이음선
plt.plot(f1, 'g.') #초록색 점
plt.plot(f2, 'bv') #파란색 역삼각형
plt.plot(f3, 'ks') #검은색 사각형
plt.show()


########################
#Subplot

x = np.arange(10)
plt.subplot(2,2,1) #2행 2열 중에 첫번째
plt.plot(x, x**2)

plt.subplot(2,2,2)
plt.plot(x, x*5)

plt.subplot(223) #2행 2열 3번째
plt.plot(x, np.sin(x))

plt.subplot(224)
plt.plot(x.np.cos(x))

#이미지 표시
#plt.plot대신 plt.imshow함수를 호출하면 opencv로 읽어들인 이미지를 그래프 영역에 출력 가능
import cv2
img = cv2.imread('0_high.jpg')
plt.imshow(img)
plt.show()

#하지만 위의 그림은 색상이 이상함. plt.imshow()함수는 컬러 이미지인 경우 컬러 채널을 RGB순으로 해석하지만 OpenCV는 BGR로 만들어져서 색상의 위치가 반대임
img = cv2.imread('0_high.jpg')
plt.imshow(img[:,:,::-1]) #이미지컬러 채널 변경해서 표시
#img[:, :, :]는 3차원의 모든 내용을 선택함. 이때 마지막 축의 길이가 3이므로 다시 img[:,:,::]로 바꿀 수있음. 이때 마지막 축의 요소의 순서를 거꾸로 뒤집기 위해서
#img[:,:, ::-1]로 쓸 수 있음 이걸 풀어쓰면 -> img[:,:,(2,1,0)]  --> RGB -> BGR로 모두 바꿔라 또는 뒤집어라!
plt.xticks([])
plt.yticks([])
plt.show()

#여러 이미지 동시 출력
img1 = cv2.imread('0_high.jpg')
img2 = cv2.imread('1_high.jpg')
img3 = cv2.imread('photo.jpg')

plt.subplot(1,3,1)
plt.imshow(img1[:,:,(2,1,0)])
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2) #1행 3열 중 2번째
plt.imshow(img1[:,:,(2,1,0)])
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(img1[:,:,(2,1,0)])
plt.xticks([])
plt.yticks([])

<<<<<<< HEAD
plt.show()
=======
plt.show()
>>>>>>> d3d18406b7abc35d4b16318b939f586eb003c0da
