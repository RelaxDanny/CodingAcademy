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


# 4. 글씨 그리기
img = cv2.imread('white.JPG')

cv2.putText(img, "Plain", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0)) 

# 5. 창 관리 -> 한 개 이상의 이미지를 여러 창에 띄우거나 각 창에 키보드와 마우스 이벤트를 처리하려면 창을 관리해야함

file_path = 'white.JPG'
img = cv2.imread(file_path)
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)

cv2.imshow('origin', img)
cv2.imshow('gray', img_gray)

cv2.moveWindow('origin', 0,0)
cv2.moveWindow('gray', 100, 100) #창 위치 변경

cv2.waitKey(0)
cv2.resizeWindow('origin', 200, 200)
cv2.resizeWindow('gray', 100,100)

cv2.waitKey(0)
cv2.destroyWindow("gray")

cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. 키보드 이벤트 
img_file = 'white.jpg'
img = cv2.imread(img_file)
title = "IMG"
x, y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력을 무핟내기, 8비트 마스크 처리
    print(key, chr(key))
    if key == ord('w'):
        y -= 10
    elif key == ord('s'):
        y += 10
    elif key = ord('a'):
        x -= 10
    elif key = ord('d'):
        x += 10
    elif key == ord('q') or key == 27: #q or ESC
        break
        cv2.destroyAllWindows()
    cv2.moveWindow(title,x, y)

# 7. 마우스 이벤트로 동그라미 그리기
title = 'mouse event'
img = cv2.imread('white.jpg')
cv2.imshow(title, img)

def onMouse(event, x, y , flags, param):
    print(event, x, y, )
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 30, (0,0,0), -1) #지름이 30픽셀인 검은색 원을 해당 좌표에 그림
        cv2.imshow(title, img)
cv2. setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()

# 8. 플래그를 이용한 동그라미 그리기
title = 'mouse event'                   # 창 제목
img = cv2.imread('../img/blank_500.jpg') # 백색 이미지 읽기
cv2.imshow(title, img)                  # 백색 이미지 표시

colors = {'black':(0,0,0),
         'red' : (0,0,255),
         'blue':(255,0,0),
         'green': (0,255,0) } # 색상 미리 정의

def onMouse(event, x, y, flags, param): # 아무스 콜백 함수 구현 ---①
    print(event, x, y, flags)                # 파라미터 출력
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 버튼 누름인 경우 ---②
        # 컨트롤키와 쉬프트 키를 모두 누른 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY : 
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY : # 쉬프트 키를 누른 경우
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY : # 컨트롤 키를 누른 경우
            color = colors['red']
        # 지름 30 크기의 검은색 원을 해당 좌표에 그림
        cv2.circle(img, (x,y), 30, color, -1) 
        cv2.imshow(title, img)          # 그려진 이미지를 다시 표시 ---③

cv2.setMouseCallback(title, onMouse)    # 마우스 콜백 함수를 GUI 윈도우에 등록 ---④

while True:
    if cv2.waitKey(0) & 0xFF == 27:     # esc로 종료
        break
cv2.destroyAllWindows()

# 9. 트랙바
import numpy as np

win_name = 'Trackbar'                                   # 창 이름

img = cv2.imread('../img/blank_500.jpg')
cv2.imshow(win_name,img)                                # 초기 이미지를 창에 표시

# 트랙바 이벤트 처리 함수 선언 ---①
def onChange(x):                                        
    print(x)                                            # 트랙바 새로운 위치 값 --- ②
    # 'R', 'G', 'B' 각 트랙바 위치 값    --- ③
    r = cv2.getTrackbarPos('R',win_name)               
    g = cv2.getTrackbarPos('G',win_name)               
    b = cv2.getTrackbarPos('B',win_name)               
    print(r, g, b)
    img[:] = [b,g,r]                                    # 기존 이미지에 새로운 픽셀 값 적용 --- ④
    cv2.imshow(win_name, img)                           # 새 이미지 창에 표시

# 트랙바 생성    --- ⑤
cv2.createTrackbar('R', win_name, 255, 255, onChange)  
cv2.createTrackbar('G', win_name, 255, 255, onChange)
cv2.createTrackbar('B', win_name, 255, 255, onChange)

while True:
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows() 