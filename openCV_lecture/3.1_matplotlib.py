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
