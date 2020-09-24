import cv2
import numpy as np

win_name = "scan"

#이미지 읽기
img = cv2.imread("img/paper.jpg")
cv2.imshow('original', img)
cv2.waitKey(0)
draw = img.copy()

#그레이 스케일 변환 및 케니 엣지
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3,3), 0) #가우시안 블러로 노이즈 제거
edged = cv2.Canny(gray, 75, 200) #캐니 엣지로 경계 검출
cv2.imshow(win_name, edged)
cv2.waitKey(0)

#컨투어 찾기
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#find countour 함수로 컨투어를 찾아서 그 영역이 가장 큰 컨투어를 골라 approxPolyDP함수로
#단순화한 뒤에 꼭짓점 4개를 구함

#모든 컨투어 그리기
cv2.drawContours(draw, cnts, -1, (0,255,0))
cv2.imshow(win_name, draw)
cv2.waitKey(0)

#컨투어들 중에 영역 크기순으로 정렬
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
for c in cnts:
    #영역이 가장 큰 컨투어 부터 근사 컨투어 단순화
    peri = cv2.arcLength(c, True) #둘레길이
    #둘레 길이의 0.02 근사 값으로 근사화
    vertices = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(vertices) == 4: #근사한 꼭짓점이 4개면 중지
        break
pts = vertices.reshape(4,2) # N x 1 x 2 배열을 4x2로 조정
for x,y in pts:
    cv2.circle(draw, (x,y), 10, (0,255,0), -1) #좌표에 동그라미 표시
cv2.imshow(win_name, draw)
cv2.waitKey(0)
merged = np.hstack((img, draw))

#좌표 4개 중 상하좌우 찾기
sm = pts.sum(axis=1) #4쌍의 좌표 각각 x+y 계산
diff = np.diff(pts, axis =1) #4쌍의 좌표 각각 x-y로 계산

topLeft = pts[np.argmin(sm)] #x + y가 가장 작은 값이 좌상단좌표
bottomRight = pts[np.argmax(sm)]
topRight = pts[np.argmin(diff)]
bottomLeft = pts[np.argmax(diff)]

#변환 전 4개 좌표
pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

#변환 후 영상에 사용 할 서류의 폭과 높이 계산
w1 = abs(bottomRight[0] - bottomLeft[0])
w2 = abs(topRight[0] - topLeft[0])
h1 = abs(topRight[1] - bottomRight[1])
h2 = abs(topLeft[1] - bottomLeft[1])
width = max([w1,w2])
height = max([h1,h2])

#변환 후 4개의 좌표
pts2 = np.float32([[0,0], [width-1,0],[width-1, height-1],[0, height-1]])

#변환 행렬 계산
mtrx = cv2.getPerspectiveTransform(pts1, pts2)

#원근 변환 적용
result = cv2.warpPerspective(img, mtrx, (width, height))
cv2.imshow(win_name, result)
cv2.waitKey(0)
cv2.destroyAllWindows()

