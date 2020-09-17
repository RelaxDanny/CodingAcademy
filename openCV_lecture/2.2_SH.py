import cv2

# 1. 다양한 선 그리기
img = cv2.imread('white.jpg')

#cv2.line(img, start, end, color, [, thickness = 1, lineType])
# cv2.line(img, (50,50), (150,50), (250, 0,0)) #파란색 1픽셀짜리 선

# cv2.line(img, (100,100), (400,100), (255,255,0), 10) #파란색 10픽셀 짜리 선

# cv2.line(img, (100,350), (400,400), (0,0,255), 1, cv2.LINE_4) #브레젠햄 알고리즘을 통한 선긋기

# cv2.line(img, (100,400), (400,450), (0,0,255), 1)


# cv2.line(img, (100,450), (400,500), (0,0,255), 1, cv2.LINE_AA)

# # 2. 사각형 그리기
# cv2.rectangle(img, (50,50), (150,150), (255,0,0)) #좌, 상 우 하 좌표로 사각형 그리기
# cv2.rectangle(img, (50,50), (150,150), (255,0,0), -1, cv2.LINE_AA)

# cv2.imshow('lines', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 3. 다각형 그리기
import numpy as np 

#번개모양 선 좌표
# pts1 = np.array([[50,50],[150,150],[100,140],[200,240]], dtype = np.int32)
# # 삼각형
# pts2 = np.array([[350,50],[250,250],[450,200]], dtype = np.int32)

# print(pts1)
# cv2.polylines(img, [pts1], False, (255,0,0), 10, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, (0,255,0), 10, cv2.LINE_AA)

# cv2.imshow('polyline', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 4. 글씨를 창에 띄우기
# img = cv2.imread("white.jpg")
# cv2.putText(img, "KSH", (50, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 4)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 5. 창을 관리하는법 

# f = 'photo.jpg'
# img = cv2.imread(f)
# img_gray = cv2.imread(f, cv2.IMREAD_GRAYSCALE)

# cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('gray', cv2.WINDOW_NORMAL)

# cv2.imshow('origin', img)
# cv2.imshow('gray', img_gray)

# cv2.moveWindow('origin', 0,0)
# cv2.moveWindow('gray', 100, 100)

# cv2.waitKey(0)
# cv2.resizeWindow('origin', 200,200)
# cv2.resizeWindow('gray', 100, 100) # W, H

# cv2.destroyAllWindows()

# 6. 키보드 이벤트
# i = "white.jpg"
# img = cv2.imread(i)
# title = 'IMG'
# x, y = 100, 100

# while True:
#     cv2.imshow(title, img)
#     cv2.moveWindow(title, x, y)
#     key = cv2.waitKey(0) & 0xFF # 8비트 처리를 하겠다 
#     print(key, chr(key))
#     if key == ord('w'):
#         y -= 50
#     elif key == ord('s'):
#         y += 50
#     elif key == ord('a'):
#         x -= 50
#     elif key == ord('d'):
#         x += 50
#     elif key == 27: #ESC
#         break
#         cv2.destroyAllWinodws()
#     cv2.moveWindow(title, x, y)

# 7. 마우스 이벤트를 이용하여 동그라미 그리기
# title = "mouse event"
# i = cv2.imread('white.jpg')
# cv2.imshow(title, i)

# colors = {
#             'black' : (0,0,0),
#             'red'   : (0,0,255),
#             'blue'  : (255,0,0),
#             'green' : (0,255,0)}

# def onMouse(event, x, y, flags, param):
#     print(event, x, y, flags)
#     color = colors['black']
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
#             color = colors['green']
#         elif flags & cv2.EVENT_FLAG_CTRLKEY:
#             color = colors['blue']
#         elif flags & cv2.EVENT_FLAG_SHIFTKEY:
#             color = colors['red']
#         cv2.circle(i, (x,y), 30, color, -1) # 지름 30 px, -1 속을 채워라
#         cv2.imshow(title, i)

# cv2.setMouseCallback(title, onMouse)

# while True:
#     if cv2.waitKey(0) & 0xFF == 27:
#         break

# cv2.destroyAllWindows()

#9. 트랙바
import numpy as np

win_name = "track bar"

img = cv2.imread('white.jpg')
cv2.imshow(win_name, img)

def onChange(x):
    print(x)
    r = cv2.getTrackbarPos('R', win_name)
    g = cv2.getTrackbarPos('G', win_name)
    b = cv2.getTrackbarPos('B', win_name)
    print(r, g, b)
    img[:] = [b,g,r]
    cv2.imshow(win_name, img)

#트랙바 생성
cv2.createTrackbar('R', win_name, 255, 255, onChange)
cv2.createTrackbar('G', win_name, 255, 255, onChange)
cv2.createTrackbar('B', win_name, 255, 255, onChange)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()