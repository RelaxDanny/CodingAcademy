import numpy as np

np.random.seed(0) 

# Input은 거의 X로 표시
# 4 features
X = [[1, 2, 3, 2.5],
    [2, 5, -1, 2],
    [-1.5, 2.7, 3.3, -0.8]]

"""
우리가 모델을 저장하고 그에 대해서 쓴다는뜻은 결국
이전에 배운 bias와 weights를 그대로 적용한다는 말
"""

# New Network 구성
# 보통 weight를 구성할때 -1 ~ 1사이 값으로 하고 tight할 수록 좀 좋은 영향이 있음
# weight가 1을 넘게 되면 점점 커져서 사실 range를 벗어나게 돼서 explosion 현상이 일어남 
# 최대한 -1 ~ 1 사이에 결과값이 있는게 좋음 -> scaling and normalization 사용 하는 이유
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons): # n_inputs = how many features?
        # 연산 수를 줄이기 위해 Transpose를 하지 않고 바로 weight의 shape을 계산에 맞게 넣어주기
        self.weights = np.random.randn(n_inputs, n_neurons) # Shape를 적어야 함 (What is the size of input?) (인풋갯수, 뉴론 갯수)
        self.biases = np.zeros((1, n_neurons)) # (1, 뉴론갯수)
        
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases # dot production

layer1 = Layer_Dense(4, 5) # 뉴론 갯수 맘대로 
layer2 = Layer_Dense(5, 2) # 여기서는 layer1의 결과값이 결국 layer2의 input이 되니 dot production이 적용된 최종 크기가 input이 되어야함

layer1.forward(X)
print(layer1.output)

layer2.forward(layer1.output)
print(layer2.output)

#다음시간엔 activation function에 대해서 알려주기
# print(np.random.randn(4,3))