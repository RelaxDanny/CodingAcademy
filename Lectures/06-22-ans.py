def solution():
    answer = 0
    arr.sort(reverse=True)
    for i in range(N):
        arr[i] = arr[i] * (i + 1)
 
    return max(arr)
 
 
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
 
print(solution())

# 20
# 50
# 80
# 100
# 120

# sort => [120 100 53 51 50 20]
# list.sort(reverse=True)
# 120, 200, 240, 200, 100

# 240