"""
Algorithm
1. for loop으로 리스트를 돌면서 왼쪽값이 더 크면 swap
2. 아닐경우 아무것도 안함.
3. 마지막 값이 maximum이라는걸 아니깐 2번째 룹부터는 마지막까지 갈필요없음. -> len(listA-1)-i

*** bubble은 i만큼 iteration을 돌 때 마지막의 값은 max인걸 알기에 무시 함
"""


listA = [5, 3 ,8, 6, 7, 2]
print(listA)
def bubblesort(listA): #O(N^2)
    for i in range(0, len(listA)-1):
        for j in range(0, len(listA)-1-i):
            if listA[j] > listA[j+1]:
                #SWAP
                listA[j], listA[j+1] = listA[j+1], listA[j]
    return listA
print(bubblesort(listA))

print(sorted(listA))

"""
sorted => built in
O(log N) -> binary Search -> sorted
"""
# Data Structure 효율적으로 관리하는 한 방법
# Sorting algorithm
# 1. binary search
# 2. bubble sort
#  - insertion sort
#  - selection sort
# 3. merge sort 
#  - heap sort
#  - 
