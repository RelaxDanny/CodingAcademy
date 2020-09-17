import cv2
img = cv2.imread("dino.PNG", 1)
# print(type(img))
# print(img.ndim)
# print(img.shape)
# print(img.size)

# #input and output -> 같아야 하는 경우가 대다수.
# print(img.dtype)
# print(img.itemsize)

#1. Numpy 배열 생성
import numpy as np
# a = np.array([1,2,3,4])
# print(a)
# print(a.dtype)
# print(a.shape)

# b = np.array([[1,2,3,4],[5,6,7,8]])
# print(b)
# print(b.dtype)
# print(b.shape)
# print(b.ndim)

# c = np.array([1,2,3.14,4])
# print(c)
# print(c.dtype)
# print(c.shape)
# ls = [1,2,3,4]
# d = np.array(ls, dtype=np.float16)
# print(d)

# a = np.uint8([1,2,3,4])
# print(a)

# a = np.empty((2,3)) #2열 3행
# print(a)
# print(a.dtype)

# a.fill(255)
# print(a)

# b = np.zeros((2,3))
# print(b)
# print(b.dtype)

# c = np.zeros((2,3), dtype=np.int8)
# print(c)

# d = np.ones((2,3), dtype=np.uint8)
# print(d)

# e = np.full((2,3,4), 255) 
# print(e)

# a = np.empty_like(img)
# print(a.shape)
# print(a)
# b = np.zeros_like(img)
# print(b)
# c = np.ones_like(img)
# d = np.full_like(img, 255)
# print(d)

#순차적인 방법으로 생성, 랜덤값 방법으로 생성
# a = np.arange(5)
# print(a)
# b = np.arange(7.1)
# print(b)
# c = np.arange(3, 9, 2)
# print(c)

# 5. 난수 -> Random Number 
# print(np.random.rand()) # 0부터 1까지의 랜덤 소수를 return 
# print(np.random.randn()) #randn은 평균이 0이고 분산이 1인 정규 분포를 따르는 무작위 수 

# print(np.random.rand(2,3))
# print(np.random.randn(3,3))

# 6. 차원 변경
# # np.reshape()
# a = np.arange(6)
# print(a)
# b = a.reshape(2,3)
# print(b)
# c = np.reshape(a,(2,3))
# print(c)
# d = np.arange(132).reshape(4, -1) 
# print(d)
# print(d.shape)

# 1차원을 배열로 바꾸는법
# f = np.zeros((2,3,3))
# print(f)
# b = f.reshape(-1)
# print(b)
# print(np.ravel(f))

# Transpose [[2,2,2],
#           [3,3,3]]
# g = np.arange(10).reshape(2,-1)
# print(g)
# print(g.T)

# # 브로드 캐스팅 연산
# # [0,1,2,3,4,5]
# # [1,2,3,4,5,6]
# mylist = list(range(10))
# for i in range(len(mylist)):
#     mylist[i] = mylist[i] + 1
# print(mylist)

# a = np.arange(10)
# print(a + 1)

# a = np.arange(15)
# print(a+5)
# print(a-2)
# print(a*2)
# print(a/2)
# print(a**2)

# b = np.arange(6).reshape(2, -1)
# print(b*2)

# 배열 연산
# a = np.arange(10, 60, 10)
# print(a)
# b = np.arange(1,6)
# print(b)
# print(a + b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# al = [10,20,30,40]
# ml = [1,2,3,4,5]
# print(al + ml)

#하지만 배열간의 연산에는 shape가 완전히 동일해야 가능하다. 
#또는 하나의 배열이 1차원이면서 1차원 배열의 축의 길이 같아야 한다.
# a = np.ones((2,3))
# b = np.ones((3,2))
# b = b.T
# print(a+b)

# c = np.arange(3)
# print(a)
# print(c)
# print(a+c)

# d = np.arange(3)
# print(a + d)

# #Index와 Slicing

# a = np.arange(10)
# print(a[5])

# b = np.arange(12).reshape(3,4)
# print(b)
# print(b[1])
# print(b[1,2])

# a[5] = 9
# print(a)

# b[0] = 0
# print(b)

# b[1,2] = 90
# print(b)

# a = np.arange(10)
# print(a[2:5])
# print(a[:])

# b = np.arange(12).reshape(3,4)
# print(b)
# print(b[0:2, 1])
# print(b[0:2, 1:3])
# print(b[2, :])

# #Fancy Indexing
# a = np.arange(6)
# print(a[[5]])
# print(a[[True,False,True,False,True,False]])

# a = np.arange(10)
# b = a > 5
# print(b)
# print(a[b])
# print(a[a>5])
# a[a>5] = 1
# print(a)

#병합과 분리 

# axis -> 축 axis = 0 -> 1d array, 

# a = np.arange(4).reshape(2,2)
# print(a)
# b = np.arange(10, 14).reshape(2,2)
# print(b)

# # vstack -> vertically stack
# # hstack -> horizontally stack
# # concatenate -> concatenate

# # print(np.vstack((a,b))) 
# # print(np.hstack((a,b))) 
# print(np.concatenate((a,b), 0)) # axis = 0  2,2 -> 4,2
# print(np.concatenate((a,b), 1)) # axis = 1  2,2 -> 2,4

# a = np.arange(12).reshape(4,3)
# b = np.arange(10,130,10).reshape(4,3)
# # print(a)
# # print(b)
# # c = np.stack((a,b), 0) #axis 0을 기준으로 병합 4x3 -> 0,4,3 - > 2,4,3
# # print(c)
# # print(c.shape)

# # d = np.stack((a,b), 1)
# # print(d)
# # print(d.shape)

# e = np.stack((a,b), -1)
# print(e)
# print(e.shape)


#검색 방식
# a = np.arange(10, 20)
# # O(n)
# print(np.where(a > 15)[0])
# print(np.where(a == 15)[0])
# print(np.nonzero(a>15))
# t = np.array([True,True,True])
# print(np.all(t))
# t[1] = False
# print(np.all(t))

import cv2

# img = np.zeros((120,120), dtype = np.uint8)
# img[25:35, :] = 45
# img[55:65, :] = 115
# img[85:95, :] = 160
# img[:, 35:45] = 205
# img[:, 75:85] = 255
# cv2.imshow('Gray', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows(0)

img = np.zeros((120,120,3), dtype = np.uint8)
img[25:35, :] = [255, 0, 0]
img[55:65, :] = [0, 255, 0]
img[85:95, :] = [0, 0, 255]
img[:, 35:45] = [255, 255, 0]
img[:, 75:85] = [255, 0, 255]
cv2.imshow('color', img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)