K = int(input())
num_stack = []


for _ in range(K):
    num = int(input())
    if num == 0:
        del num_stack[-1]
    else: 
        num_stack.append(num)
if not num_stack:
    print(0)
else:
    print(sum(num_stack))

