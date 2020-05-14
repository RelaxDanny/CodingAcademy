# O(n^2) => insertion, bubble, selection, ...

# O(n log n) => Search

# 나는 숫자5의 인덱스를 찾고싶어 리스트에서. 어떻게찾을래?
#  = 4

#  Approach 1. Binary Search !! -> 빠르고, 전체를 확인하지않는 방법 66%
#      1000000000개, 

#  Brute Force: 노가다 = 전체를 확인하는 방법.
#   -> 1000000000개
# [1,2,3,4,5,6] => 숫자 5의 위치를 찾아라.
# 0번째 인덱스 부터 list[-1]의 인덱스까지 다 loop을 돌리면서 5가 나올때까지 돌려라.

def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)-1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint #index를 리턴한다.
        elif item < midpoint_value:
            end_index = midpoint - 1
        # elif item > midpoint_value:
        else:
            begin_index = midpoint + 1
    return None

sequence_a = [2,4,5,6,7,8,9]

item_a = 10

print(binary_search(sequence_a, item_a))