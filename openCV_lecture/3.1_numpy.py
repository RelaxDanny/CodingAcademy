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
