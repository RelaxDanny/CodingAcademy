#OPEN COMUTER VISION

# Image

# Video -> image의 연속된 프레임

#얻는것 : 아직 사회가 해결하지 못한 vision system 문제들의 해결 방법
#예: 카메라로만 부피를 측정, 교통 체증 파악, CCTV로 범인잡기, 자율주행(테슬라)

# 1. 이미지 파일을 화면에 표시
import cv2

# img_file = "C:/Users/danny/Documents/GitHub/CodingAcademy/openCV_lecture/0_high.jpg" #absPATH -> absolute path
# img = cv2.imread(img_file)

# if img is not None:
#     cv2.imshow('IMG', img) #위에서 읽은 이미지를 화면(창)에 표시
#     cv2.waitKey() #키가 입력이 될때까지 창을 끄지 않겠다.
#     #cv2.waitKey([delay]) delay를 0으로 두면 무한으로 대기
#     #key값을 넣으면 그 key가 입력 될때 끈다.
#     cv2.destroyAllWindows() #창을 모두 닫는다.
# else:
#     print("NO img found.")


# # 2. 이미지 파일을 GRAY 스케일로 화면에 표시
# img_file = "C:/Users/danny/Documents/GitHub/CodingAcademy/openCV_lecture/0_high.jpg" #absPATH -> absolute path
# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

# if img is not None:
#     cv2.imshow('IMG', img) #위에서 읽은 이미지를 화면(창)에 표시
#     cv2.waitKey() #키가 입력이 될때까지 창을 끄지 않겠다.
#     #cv2.waitKey([delay]) delay를 0으로 두면 무한으로 대기
#     #key값을 넣으면 그 key가 입력 될때 끈다.
#     cv2.destroyAllWindows() #창을 모두 닫는다.
# else:
#     print("NO img found.")


# # 3. 컬러 이미지를 그레이 스케일된 이미지로 저장
# img_file = "C:/Users/danny/Documents/GitHub/CodingAcademy/openCV_lecture/0_high.jpg" #absPATH -> absolute path
# save_file = "C:/Users/danny/Documents/GitHub/CodingAcademy/openCV_lecture/1_high.jpg"

# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
# cv2.imwrite(save_file, img)


# 4. 동영상 및 카메라 프레임 읽기

# video_file = "C:/Users/danny/Documents/GitHub/CodingAcademy/openCV_lecture/test.avi"

# cap = cv2.VideoCapture(video_file) #동영상 캡처 객체 생성

# if cap.isOpened():
#     while True:
#         ret, img = cap.read() #ret = True or False 비디오가 있냐 없냐 // img =  각각의 프레임 pixel값
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         if ret:
#             cv2.imshow(video_file, img)
#             cv2.waitKey(25) # 40fps
#         else:
#             break
# else:
#     print("can't open video")
# cap.release()
# cv2.destroyAllWindows()

# # 5. 내 카메라 프레임 가져오고 읽기

# cap = cv2.VideoCapture(0)
# if cap.isOpened():
#     while True:
#         ret, img = cap.read()
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         if ret:
#             cv2.imshow('cam', img)
#             if cv2.waitKey(1) != -1: #1ms 동안 키 입력을 대기
#                 break
#         else:
#             print('no cam')
#             break
# else:
#     print("can't open video")
# cap.release()
# cv2.destroyAllWindows()

# 6. FPS를 지정해서 동영상 재생
# video_file = 'test.avi'

# cap = cv2.VideoCapture(video_file)
# if cap.isOpened():
    

#     while True:
#         fps = cap.get(cv2.CAP_PROP_FPS) #프레임 수 구하기
#         delay = int(1000/fps)
#         print("FPS:", fps, "Delay:", delay,"ms") #f = float, d = decimal
#         ret, img = cap.read()
#         if ret:
#             cv2.imshow(video_file, img)
#             cv2.waitKey(delay)
#         else:
#             break
# else:
#     print("no video")
# cap.release()
# cv2.destroyAllWindows()

# 7. 카메라 프레임 크기 설정
# video_file = 'test.avi'

# cap = cv2.VideoCapture(0)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print("org", width, height)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print("new:", width, height)

# if cap.isOpened():
#     while True:
#         ret, img = cap.read()
#         if ret:
#             cv2.imshow('cam', img)
#             if cv2.waitKey(1) != -1:
#                 break
#         else:
#             break
# else:
#     print("no cam")
# cap.release()
# cv2.destroyAllWindows()

# 8. 웹캠으로 사진 찍기

# cap = cv2.VideoCapture(0)

# if cap.isOpened():
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow('cam', frame)
#             if cv2.waitKey(1) != -1:
#                 cv2.imwrite('photo.jpg', frame)
#                 break
#         else:
#             break
# else:
#     print('no cam')
# cap.release()
# cv2.destroyAllWindows()

# 9. 카메라로 녹화하기
cap = cv2.VideoCapture(0)

if cap.isOpened():
    file_path = 'record.avi'
    fps = 25.40
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') #인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    out = cv2.VideoWriter(file_path, fourcc, fps, size)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('record', frame)
            out.write(frame) #파일 저장
            if cv2.waitKey(int(1000/fps)) != -1:
                break
        else:
            break
    out.release()
else:
    print('no cam')
cap.release()
cv2.destroyAllWindows()
