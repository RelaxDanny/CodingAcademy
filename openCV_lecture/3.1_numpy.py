
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
print("*" * 30)

# ---------------------- 08-24 할 차례
#5. 난수
print(np.random.rand()) # rand는 0과 1사이 값을 무작위로
print(np.random.randn()) #randn은 평균이 0 이고 분산이 1인 정규 분포를 따르는 무작위 수 mean = 1, distribution = 0

a = np.random.rand(2,3) # 2x3의 배열 생성
print(a)
b = np.random.randn(2,3)
print(b)

#6 정말 중요한 차원 변경!!!
#원래 1차원 이엿던 배열을 2열 3행으로 바꾼다던지 100x200x3인 배열을 1차원으로 바꾸는 식의 작업
a = np.arange(6)
print(a)
b = a.reshape(2,3) # a를 2x3 배열로 변경
print(b)
c = np.reshape(a, (2,3)) #이런식으로도 표현 가능 결과는 같다
print(c)
d = np.arange(100).reshape(2, -1) #2차원으로 만들되, -1을 넣음으로서 해당 차수에 대해서는 크기 지정을 안할태니 알아서 계산 하라는 뜻
print(d)
print(d.shape)
e = np.arange(100).reshape(-1,5) #5개로 나누되, 행의 크기는 알아서 나누기 하지만 홀수값 예를들어 arange가 101이 균일하게 나오면 나눌 수 없어서 에러가 나옴
print(e)
print(e.shape)
#1차원 배열로 바꾸는법은 reshape과 ravel이 있음
f = np.zeros((2,3))
print(f)
f.reshape((6,)) #2x3이 6이니깐 1차원은 행과 열을 다 곱하면됨 
print(f)
f.reshape(-1) # 하지만 귀찮으니 -1만 보내주자
print(f)
print(np.ravel(f))

# ndarray.T로 Transpose 행과 열을 바꾸어라!
g = np.arange(10).reshape(2, -1)
print(g)
print(g.T) #이게 끝.. 

# 브로드 캐스팅 연산
# 넘파이를 사용하는 가장 큰 이유
mylist = list(range(10))
for i in range(len(mylist)):
    mylist[i] = mylist[i] + 1
print(mylist)
#하지만 넘파이는
a = np.arange(10)
print(a + 1)

a = np.arange(15)
print(a+5)
print(a-2)
print(a*2)
print(a/2)
print(a**2)
b = np.arange(6).reshape(2, -1)
print(b*2) # N-dimension에도 똑같이 적용 됨

#브로드 캐스팅 비교연산
print(a)
print(a>2) #a 가 2보다 크면 True else False

#배열끼리의 연산
a = np.arange(10, 60, 10)
b = np.arange(1, 6)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
#하지만 배열간의 연산에는 shape이 완전히 동일 해야 가능함 또는 하나의 배열이 1차원이면서 1차원 배열의 축의 길이가 같아야 함
a = np.ones((2,3))
b = np.ones((3,2))
print(a+b) #error occurs

c = np.arange(3)
print(a)
print(c)
print(a+c) #얘내 둘은 1차원 배열의 열의 개수가 a 배열의 열의 개수와 같아서 계산 가능

d = np.arange(2)
print(a + d) # error

d = np.arange(2).reshape(2,1) # 이렇게 reshape 해주면 가능
print(a + d)

#인덱싱과 슬라이싱

a = np.arange(10)
print(a[5])

b= np.arange(12).reshape(3,4)
print(b[1])
print(b[1,2]) #이런식으로 comma로 처리할 수 있음 list에서의 b[1][2] 같음
a[5] = 9
print(a)
b[0] = 0
print(b) #1열의 값들이 모두 0으로 바뀜 브로드캐스팅 연산
b[1,2] = 90
print(b)
b[1][2] = 89
print(b)

a = np.arange(10)
print(a[2:5]) #list 와 같음
print(a[:])
b = np.arange(12).reshape(3,4)
print(b[0:2, 1]) #[1,5] 각각의 0, 1 row에서 1번째 인덱스
print(b[0:2, 1:3]) #[1,2],[5,6] #2차원으로 나오게 됨 0, 1 row에서 1부터 2까지의 인덱스
print(b[2, :]) # 2번 row에서 모든 값
print(b[:, 1])
print(b[0:2, 1:3])

#만약 파이썬 리스트처럼 복제본을 얻고싶다면 ndarray.copy()를 쓰면 됨 a = b가아니라 copy!

#팬시 인덱싱 -> 배열 인덱스에 다른 배열을 전달해서 원하는 요소를 선택하는 방법
a = np.arange(5)
print(a[[1,3]])
print(a[[True, False, True, False, True]]) #이렇게되면 True에 속하는 인덱스만 뽑게 됨

a = np.arange(10)
b = a > 5
print(b) #boolean 값을 가진 어레이 return
print(a[b]) #[6,7,8,9] 이거는 위에서 배운 a[[True, False, True, False]]와 같음
print(a[a>5])
a[a>5] = 1 #5보다 큰값은 1로 교체
print(a)



######################################################
#병합과 분리

#axis는 축이다 (1,1,1) 이런 배열이 있을경우 각 axis는 index처럼 0, 1, 2의 axis로 표현 => 3개의 축
a = np.arange(4).reshape(2,2)
print(a)
b = np.arange(10,14).reshape(2,2)
print(b)
print(np.vstack((a,b))) # vertical
print(np.hstack((a,b))) # horizontal
print(np.concatenate((a,b), 0)) # a,b arrays를 0번째 축 기준으로 병합 (2,2)에다가 0번째 축을 기준이라면 (4,2)가 된다.
print(np.concatenate((a,b), 1)) #1번축 기준으로 병합 (2,2)에서 1번째 축을 기준 -> (2,4)

a = np.arange(12).reshape(4,3)
b = np.arange(10, 130, 10).reshape(4,3)
print(a)
print(b)
c = np.stack((a,b), 0) #0번 축을 기준으로 배열을 병합
print(c)
print(c.shape) # 2,4,3

d = np.stack((a,b), 1) #1번 축
print(d.shape) # 4,2,3
print(d)

e = np.stack((a,b), 2) #4,3,2
print(e.shape)
print(e)

f = np.stack((a,b), -1) #맨 마지막 axis를 기준
print(f.shape)

#배열 분리
# a = np.arange(12)
# print(np.hsplit(a, 3)) #3개의 1d array로 수평 분리
# print(np.hsplit(a, [3,6])) #각 어레이들을 0:3, 3:6, 6:로 나눈다
# print(np.hsplit(a, [3,6,9])) # 0:3, 3:6, 6:9 그리고 나머지
# print(np.split(a, 3, 0)) #0은 축을 의미함. 3은 나눌 개수
# print(np.split(a, [3,6,9], 0))

# b = np.arange(12).reshape(4,3)
# print(b)
# print(np.vsplit(b, 2))# vertical array 2개로 나누기
# print(np.split(b, 2, 0))
# print(np.hsplit(b, [1]))
# print(np.split(b, [1], 1))

#검색 -> 수많은 데이터를 쉽고 빠르게 다루려는 이유에서 numpy를 많이들 씀
a = np.arange(10, 20)
print(np.where(a>15))
print(np.where(a>15, 1, 0)) #보다 크면 1로, 아닐경우 0으로
print(a)

print(np.where(a>15, 99, a)) #아닐경우 그대로
print(np.where(a>15, a, 0)) #아닐경우 0으로
print(a)

b = np.arange(12).reshape(3,4)
print(b)
coords = np.where(b>6)
print(coords) # 2개의 축을 리턴 하는데 이걸 하나로 묶으면 x,y좌표처럼 됨
print(np.stack((coords[0], coords[1]),-1))

z = np.array(0,1,2,0,1,2)
print(np.nonzero(z))  #index를 리턴함

zz = np.array([[0,1,2],[1,2,0],[2,0,1]])
coods = np.nonzero(zz)
print(coords)
print(np.stack((coords[0], coords[1]) -1))

print(np.nonzero(a>15))
print(np.where(a>15))
print(np.nonzero(b>6))
print(np.where(b>6))


#Numpy 배열에 모든 요소가 참또는 거짓인지 확인할 때
t = np.array([True, True, True])
print(np.all(t))
t[1] = False
print(np.all(t))

#all에 axis 인자를 지정하지 않으면 모든 요소에 대해서 True를 만족하는지 검색
tt = np.array([[True,True], [False, True], [True, True]])
print(np.all(tt, 0)) # [False, True] 

print(np.all(tt, 1)) # [True, False, True]

#이미지 생성
import cv2
import numpy as np
img = np.zeros((120,120), dtype = np.uint8)
img[25:35, :] = 45
img[55:65, :] = 115
img[85:95, :] = 160
img[:, 35:45] = 205
img[:, 75:85] = 255
cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows

img = np.zeros((120,120), dtype = np.uint8)
img[25:35, :] = [255, 0, 0]
img[55:65, :] = [0, 255, 0]
img[85:95, :] = [0, 0, 255]
img[:, 35:45] = [255, 255, 0]
img[:, 75:85] = [255, 0, 255]
cv2.imshow('BGR', img)
cv2.waitKey(0)
cv2.destroyAllWindows