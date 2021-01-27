"""
1 강의에서는 Single Neron to Single Value

1. Neuron 이란 (Unit)
2. Input Layer, Hidden Layer, Output Layer

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)

"""

"""
2 강의 Multiple Neurons to Single Output

1. 인풋의 갯수와 weights는 같음
2. 각 인풋이 humidity, temperature of a class로 생각할 수 있음
3. Multiple Neurons to Single Output
4. Deep learning 현재까지의 숙제는 best tuning the network임

inputs = [1, 2, 3, 2.5] 

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2 # 한개의 neuron에는 한개의 bias만 필요함
bias2 = 3
bias3 = 0.5 

output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] +bias1,
        inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] +bias2,
        inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] +bias3]
print(output)
"""

import numpy as np 

inputs = [1.0, 2.0, 3.0, 2.5] # Shape (4,) Type: 1D array, Vector
inputs2 = [[1,5,6,2],
           [3,2,1,3]] # Shape (2, 4) Tpye: 2D Array, Matrix

inputs3 = [[[1,5,6,2],
           [3,2,1,3]], # Shape (3, 2, 4) Tpye: 3D Array, Matrix
          [[1,5,6,2],
           [3,2,1,3]],
           [[1,5,6,2],
           [3,2,1,3]]]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2.0, 3.0, 0.5]

# Dot_Product = a[0]*b[0] + a[1]*b[1] + ... + a[n]+b[n]
# output = np.dot([1,2,5,6], [0.2,0.6,-0.1,0.9])+2
layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
print(layer_outputs)

# output = np.dot(inputs, weights) + biases #이거 한 번 보여주기
output = np.dot(weights, inputs) + biases
print(output)
#위에꺼 풀어쓰면
outputs = [np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)]
print(output)