#관심영역 지정
import cv2
import numpy as np

img = cv2.imread('0_high.jpg')

#ROI = region of interest

x = 320; y = 150; w = 50; h = 50 #roi 좌표
roi = img[y:y+h, x:x+w]

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0))
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#관심영역 복제 및 새 창 띄우기
x = 320; y = 150; w = 50; h = 50 #roi 좌표
roi = img[y:y+h, x:x+w]
img2 = roi.copy() #numpy copy

img[y:y+h, x+w:x+w+w] = roi 
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0))
cv2.imshow("img", img)
cv2.imshow("roi", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
#스레시홀딩 
"""
grayscale, 즉 binary image로 표현하는 이유는 이미지에서 원하는 피사체의 모양을 좀 더 정확히 
판단하기 위함. 종이에서 글씨분리등, 배경에서 전경을 분리하는 작업
Thresholding이란, 여러 점수를 커트라인을 기준으로 합격과 불합격으로 나누는 것처럼
여러 값을 경계점을 기준으로 두 가지 분류로 나누는 것으로, 바이너리 이미지를
만드는 가장 대표적인 방법

binary img 원리 : 컬러 이미지의 각 픽셀값이 특정 경계값을 넘으면 255, 못넘으면 0으로 설정하는 작업
"""
import matplotlib.pylab as plt
img = cv2.imread('0_high.jpg', cv2.IMREAD_GRAYSCALE)

#넘파이 연산으로 binary img만들기
thresh_np = np.zeros_like(img)
thresh_np[img > 127] = 255 #127보다 큰값을 255로 변경

# openCV로 바이너리 이미지 만들기
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #127을 넘으면 255로 바꿔라
print(ret)

#원본과 결과를 같이 출력
imgs = {'Original': img, "Numpy API": thresh_np, 'cv2.threshold':thresh_cv}
for i, (key,value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap = 'gray')
    plt.xticks([])
    plt.yticks([])
plt.show()

#스레시홀드 플래그 실습
import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

imgs = {'origin':img, 'BINARY':t_bin, 'BINARY_INV':t_bininv, \
        'TRUNC':t_truc, 'TOZERO':t_2zr, 'TOZERO_INV':t_2zrinv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2,3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]);    plt.yticks([])
    
plt.show()


#Otsu -> 가장 중요한게 경계값을 얼마나 정하냐임
"""
종이위에 적힌 문자들은 확실하기 때문에 굳이 스레시홀딩이 필요없다.
하지만, 현실은 흰색, 누런색, 회색종이에 검은색, 파란색 등 다양함.
그래서 여러 차례에 걸쳐 적절한 경계값을 조금씩 수정해야함

이를 위해서 나온게 Nobuyuki Otsu의 알고리즘인 오츠 알고리즘
"""
import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지를 그레이 스케일로 읽기
img = cv2.imread('.jpg', cv2.IMREAD_GRAYSCALE) 
# 경계 값을 130으로 지정  ---①
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)        
# 경계 값을 지정하지 않고 OTSU 알고리즘 선택 ---②
t, t_otsu = cv2.threshold(img, -1, 255,  cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
print('otsu threshold:', t)                 # Otsu 알고리즘으로 선택된 경계 값 출력

imgs = {'Original': img, 't:130':t_130, 'otsu:%d'%t: t_otsu}
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()


#적응형 스레시홀드 적용

blk_size = 9        # 블럭 사이즈
C = 5               # 차감 상수 
img = cv2.imread('
../imgsudoku.png', cv2.IMREAD_GRAYSCALE) # 그레이 스케일로  읽기

# ---① 오츠의 알고리즘으로 단일 경계 값을 전체 이미지에 적용
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# ---② 어뎁티드 쓰레시홀드를 평균과 가우시안 분포로 각각 적용
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                                      cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                     cv2.THRESH_BINARY, blk_size, C)

# ---③ 결과를 Matplot으로 출력
imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, \
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,'gray')
    plt.xticks([]),plt.yticks([])

plt.show()

