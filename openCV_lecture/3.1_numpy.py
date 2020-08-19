import cv2
img = cv2.imread("white.jpg")
print(type(img)) # numpy.ndarray 형태
print(img.ndim)
print(img.shape)
print(img.size) #각 shape의 곱

#이미지 픽셀 데이터는 음수 또는 소수점이 없고 최대 크기가 255이므로 uint8을 데이터 타입으로 사용 2의 8승 / 8비트
print(img.dtype)
print(img.itemsize) #각 요소의 크기가 1바이트 임을 알리는 것


#1. Numpy 배열 생성
print("*" * 30)
print("Numpy 배열 생성")
print("*" * 30)
import numpy as np

a = np.array([1,2,3,4])
print(a)
print(a.dtype)
print(a.shape)
print("*" * 30)
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)
print(b.shape)
print("*" * 30)
c = np.array([1,2,3.14,4])
print(c)
print(c.dtype)
print("*" * 30)
print("*" * 30)
d = np.array([1,2,3,4], dtype=np.float32)
print(d)

#임의로 타입을 정해줄때
a = np.uint8([1,2,3,4])
print("*" * 30)

#2. 크기와 초기 값으로 numpy array 생성
a = np.empty((2,3)) # 쓰레기값으로 배열 생성 // 2 rows, 3 cols 2열 3행
print(a)
print(a.dtype)
print("*" * 30)

a.fill(255)
print(a)
print("*" * 30)

b = np.zeros((2,3))
print(b)
print(b.dtype)
print("*" * 30)

c = np.zeros((2,3), dtype=np.int8)
print(c)
print("*" * 30)

d = np.ones((2,3))
print(d)
print("*" * 30)

e = np.full((2,3,4), 255) #3차원 배열, 
print(e)
print("*" * 30)

# 3. 기존 image array를 이용하여 같은 shape갖는 np array 만들기
img = cv2.imread("0_high.jpg")
print(img)
print(img.shape)
print("*" * 30)

a = np.empty_like(img)
b = np.zeros_like(img)
c = np.ones_like(img)
d = np.full_like(img, 255) #Fill 할 value를 넣어주면 전체를 그 값으로 채움
print(a)
print(b)
print(c)
print(d)
print("*" * 30)

# 4.순차적인 방법으로 생성, 랜덤값 방법으로 생성
a = np.arange(5)
print(a)
print("*" * 30)
b = np.arange(5.0)
print(b)
print("*" * 30)
c= np.arange(3, 9, 2) #3부터 9까지 2번씩 건너띄우기 -> range와 같음
print(c)