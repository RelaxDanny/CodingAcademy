import cv2
# 1. 다양한 선 그리기 

img = cv2.imread('white.jpg') 

#cv2.line(img, start, end, color, [, thickness, lineType])
cv2.line(img, (50,50), (150,50), (255,0,0)) # 파란색 1픽셀 선
cv2.line(img, (200,50), (300,50), (0,255,0)) #Green
cv2.line(img, (350,50), (450,50), (0,0,255)) # Red

cv2.line(img, (100,100), (400,100), (255,255,0), 10) #10 픽셀 선
cv2.line(img, (100,150), (400,150), (255,0,255), 10)
cv2.line(img, (100,200), (400,200), (0,255,255), 10)

cv2.line(img, (100,350), (400,400), (0,0,255), 20, cv2.LINE_4)
cv2.line(img, (100,400), (400,450), (0,0,255), 20, cv2.LINE_8) #브레젠햄 알고리즘으로 연결하는 선 차이는 없음
cv2.line(img, (100,450), (400,500), (0,0,255), 20, cv2.LINE_AA) #가우시안 필터를 이용한 계단 현상 없는거

cv2.line(img, (0,0), (500,500), (0,0,255))

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 사각형 그리기
img = cv2.imread('white.jpg')

# cv2.rectangle(img, (start), (end), color[,thickness, lineType])
cv2.rectangle(img, (50,50), (150,150), (255,0,0)) #좌상, 우하 좌표로 사각형 그리기
cv2.rectangle(img, (300,300), (100,100), (0,255,0), 10) 
cv2.rectangle(img, (450,200), (200,450), (0,0,255), -1) # -1을 하게 되면 사각면 전체를 color화 시킴

cv2.imshow('rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 다각형 그리기
import numpy as np

img = cv2.imread('white.jpg')
#numpy 배열로 좌표 생성
#번개모양 선 좌표
pts1 = np.array([[50,50],[150,150],[100,140],[200,240]], dtype = np.int32)
#삼각형 좌표
pts2 = np.array([[350,50],[250,250],[450,200]], dtype = np.int32)
#삼각형 좌표
pts3 = np.array([[150,300],[50,450],[250,450]], dtype = np.int32)
#5각형 좌표
pts4 = np.array([[350,250],[450,350],[400,450],[300,450],[250,350]], dtype = np.int32)

#좌표대로 그리기
#cv2.polylines(img, points, isClosed, color[,thickness, lineType])
cv2.polylines(img, [pts1], False, (255,0,0)) #번개모양 선
cv2.polylines(img, [pts2], False, (0,0,0), 10) #3각형 열린 선
cv2.polylines(img, [pts3], True, (0,0,255), 10) #3각형 닫힌 선
cv2.polylines(img, [pts4], True, (0,0,0)) #5각형 닫힌 선

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
