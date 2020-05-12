# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

n = int(input())

weight_list = []
height_list = []

for i in range(n):
    weight, height = map(int,input().split())
    weight_list.append(weight)
    height_list.append(height)

for i in range(len(weight_list)):
    rank = 1
    for j in range(len(weight_list)):
        if weight_list[i] < weight_list[j] and height_list[i] < height_list[j]:
            rank += 1
    print(rank, end = ' ')
