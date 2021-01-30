# 1 이미지 파일을 화면에 표시
import cv2

img_file = "0_high.jpg" #표시할 이미지 경로
img = cv2.imread(img_file) #이미지를 읽어서 img 변수에 할당

if img is not None:
    cv2.imshow('IMG', img) #읽은 이미지를 화면에 표시
    cv2.waitKey() #키가 입력될때까지 대기
    #cv2.waitKey([delay]) delay를 0으로 놓을경우 무한대기
    #특정 키를 받을 수 있다.
    cv2.destroyAllWindows() #창 모두 닫기
else:
    print("No image file")


# 2 이미지 파일을 그레이 스케일로 화면에 표시
import cv2

img_file = "0_high.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE) #두번째 매개변수에는 색을 정할 수 있음

if img is not None:
    cv2.imshow('IMG', img) #읽은 이미지를 화면에 표시
    cv2.waitKey() #키가 입력될때까지 대기
    #cv2.waitKey([delay]) delay를 0으로 놓을경우 무한대기
    #특정 키를 받을 수 있다.
    cv2.destroyAllWindows() #창 모두 닫기
else:
    print("No image file")

# 3 컬러(원본) 이미지를 그레이 스케일된 이미지로 저장

import cv2

img_file = "0_high.jpg"
save_file = "new_0_high.jpg"

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)
cv2.imwrite(save_file, img) #파일로 저장, 포맷은 확장자에 따라 달라짐
cv2.waitKey()
cv2.destroyAllWindows()

# 4 동영상 및 카메라 프레임 읽기

import cv2

video_file = 'test.avi' #동영상 파일 경로

cap = cv2.VideoCapture(video_file) #동영상 캡쳐 객체 생성
if cap.isOpened():
    while True:
        ret, img = cap.read() #다음 프레임 읽기 / img는 카메라가 보는 프레임 또는 사진 / 영상은 사진의 빠른 나열
        if ret: #ret은 카메라가 열렸는지 아닌지를 표기하는 T and F이다.
            cv2.imshow(video_file, img) #화면에 표시
            cv2.waitKey(25) #25ms지연, 40fps 정도?
        else:
            break
else:
    print("can't open video")
cap.release() #캡쳐 자원 반납 비디오 끄기
cv2.destroyAllWindows()

# 5 동영상 카메라 프레임 읽기

import cv2

cap = cv2.VideoCapture(0) #0번 카메라 장치 연결
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1: #1ms 동안 키 입력 대기
                break  #아무 키나 누르면 중지
        else:
            print("no cam")
            break
else:
    print("can't open camera")
cap.release()
cv2.destroyAllWindows()




# 6 FPS를 지정해서 동영상 재생

import cv2
video_file = ''

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
    delay = int(1000/fps)
    print("FPS: %f, Delay: %dms" %(fps, delay))
    
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)
        else:
            break
else:
    print("can't open")
cap.release()
cv2.destroyAllWindows()
#하지만 FPS속성을 카메라 장치로부터 읽을때 정상적인 값을 가져오지 못함.
#읽은 영상이 너무 고화질일 경우 픽셀 수가 많아 연산시간이 오래걸림
#이를 위해 영상 폭과 높이를 줄일 수 있음. (픽셀을 줄임)

# 7 카메라 프레임 크기 설정
import cv2

cap = cv2.VideoCaputre(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Original width: d%, height: d%" % (width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGTH, 240)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Resized width: d%, height: d%" % (width, height))

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
else:
    print("can't open")
cap.release()
cv2.destroyAllWindows()

# 8. 카메라로 사진 찍기 
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera', frame)
            if cv2.waitkey(1) != -1: #아무키나 누르면
                cv2.imwrite('photo.jpg', frame)
                break
        else:
            break
else:
    print("no cam")
cap.release()
cv2.destroyAllWindows()

# 9. 카메라로 녹화하기
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    file_path = "record.avi"
    fps = 25.40
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') #인코딩 포맷 문자 #비디오 인코딩 형식 4글자 -> MJPG, DIVX등등
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height)) #Frame 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) #비디오 writer 객체 생성 // 저장할 파일 이름, 4글자 인코딩 이름, fps, 프레임 사이즈
    #http://fourcc.org/codecs.php 에서 코덱 확인 ㄱㄱ
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('cam-record', frame)
            out.write(frame) #파일 저장
            if cv2.waitKey(int(1000/fps)) != 1:
                break
        else:
            break
    out.release()
else:
    print("no cam")
cap.release()
cv2.destroyAllWindows()

