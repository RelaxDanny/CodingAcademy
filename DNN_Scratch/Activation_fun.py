 
"""
1. 가장 먼저 Step function 이라는 함수를 Activation Function으로 사용

모든 뉴론 결과값의 합이 y

y = 1, x > 0
or
y = 0, x <= 0


2. Sigmoid

y = 1 / 1+e^-x
-> Step하고 비슷하지만, 0 과 1사이 값이 결과 값으로 나오기 때문에 
이 함수를 통해 조금더 정확한 weight, bias, input의 관게를 볼 수 있음 


3. ReLU (Rectified Linear Activation function)
y = x, x > 0
y = 0, x <= 0
음수면 무조건 결과값이 0이고 양수일때먄 그 값을 인정함 
-> 매우 빠름

4. Tanh


그래서 왜 씀??
 -> 그래프위에 여러개의 데이터를 그려보자
 -> 만약 linear function만 있었다면, 여러개의 데이터를 나눌 방법이 없을 것이다.
 -> 기본적으로 classify가 되어야 하기 때문에 non-linear activation을 써야함 

"""

import numpy as np

np.random.seed(0) 

# Input은 거의 X로 표시
# 4 features
X = [[1, 2, 3, 2.5],
    [2, 5, -1, 2],
    [-1.5, 2.7, 3.3, -0.8]]

# inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]
# output = []

# # ReLU activation fuinction
# for each in inputs:
#     if each > 0:
#         output.append(each)
#     elif each <= 0:
#         output.append(0)
#     # 또는
#     # output.append(max(0, i))
# print(output)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons): 
        self.weights = np.random.randn(n_inputs, n_neurons) 
        self.biases = np.zeros((1, n_neurons)) 
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases 


class Activation_ReLU: #Rectified Linear Unit
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)




layer1 = Layer_Dense(4, 5) # 뉴론 갯수 맘대로 
layer2 = Layer_Dense(5, 2) # 여기서는 layer1의 결과값이 결국 layer2의 input이 되니 dot production이 적용된 최종 크기가 input이 되어야함

layer1.forward(X)
print(layer1.output)

layer2.forward(layer1.output)
print(layer2.output)

#다음시간엔 activation function에 대해서 알려주기
# print(np.random.randn(4,3))
