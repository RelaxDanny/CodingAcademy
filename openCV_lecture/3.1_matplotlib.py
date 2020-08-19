# 1. plt 그림 그리기 
import matplotlib.pyplot as plt
import numpy as np

a = np.array([2,6,7,3,12,8,4,5])
plt.plot(a)
plt.show()

# 2. y = x^2 그래프 그리기
x = np.arange(10) # 0,1,2,3,4,5,6,7,8,9
y = x **2
plt.plot(x,y)
plt.show()


# 3. plot의 색 지정
x = np.arange(10)
y = x **2
plt.plot(x,y, "r") # b, g, r, c(Cyan청록색), m(Magenta 자홍색), y(yellow), k(black), w(white)


# 4 다양한 스타일 지정
"""
- : 실선 
-. : 점 이음선
. : 점
o : 원
^ : 정삼각형
> : 우 삼각형
2 : 작은 정삼각형
4 : 작은 우 삼각형
p : 오각형
h : 육각형
D : 다이아몬드 표
-- : 이음선
: : 점선
, : 픽셀
v : 역삼각형
< : 좌 삼각형
1 : 작은 역삼각형
3 : 작은 좌 삼각형
s : 사각형
* : 별표
+ : 더하기 표
x : 엑스 표
"""
x = np.arange(10)
print(x + 5)
f1 = x + 5
f2 = x ** 2
f3 = x **2 + x*2

plt.plot(x, 'r--') #빨간색 이음선
plt.plot(f1, 'g.') #초록색 점
plt.plot(f2, 'bv') #파란색 역삼각형
plt.plot(f3, 'ks') #검은색 사각형
plt.show()