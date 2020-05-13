"""
1. 맨처음놈을 minimum이라고 지정을 잠깐 한다.
2. iteration을 돌린다. 돌리면서 새로운 minimum을 select.

"""

def selection_sort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
    return A

A = [6,2,4,6,7,8,98,122,1,2,4,6,65]


print(selection_sort(A))