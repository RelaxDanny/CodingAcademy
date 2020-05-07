"""

1. set the first value as Minimum value and iterate through to find the new min.
2. after the iteration is finished, put the minimum value to the first index and start from the next
index. 
3. Repeat
"""

def selection_sort(A):
    for i in range(0, len(A)-1):
        minIndex = i # 계속 해서 A[i]를 미니멈 인덱스로 생각한다.
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:  #만약 min이 바뀌었다면(새로운 값으로)
            A[i], A[minIndex] = A[minIndex], A[i] #기존의 i 인덱스와 min의 값을 바꿔라
    return A
A = [6,2,4,6,7,8,89,1,2,5]

print(selection_sort(A))