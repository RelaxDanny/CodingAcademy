"""
7 8 5 4 9 2

5 7 8 4 9 2

1. 두번째를 지정, 두번째랑 두번째의 -1 인덱스를 비교 후 더 작은지 확인
만약 왼쪽 값이 더 작다면 그대로있고 크면 swap.

2. 두번째 j에서도 계속 같은 걸 반복 하면서 자기의 자리를 찾기

"""

def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1): #-1 은 마지막 인덱스 i-1 부터 마지막 인덱스 까지 increment by -1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1] , A[j]
            else:
                break
    return A

A = [5,1,2,7,9,3,7,0]

print(insertion_sort(A))
