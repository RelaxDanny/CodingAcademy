"""

주의: Binary Search를 사용할 것

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 

정수 M개가 주어졌을 때, 

이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

첫째 줄에 입력으로 주어진 M개의 수에 대해서, 

각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

예제 입력:
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

예제 출력:
3 0 0 1 2 0 0 2
"""
# def binary_search(sequence, item):
#     begin_index = 0
#     end_index = len(sequence)-1

#     while begin_index <= end_index:
#         midpoint = begin_index + (end_index - begin_index) // 2 # begin index +rest of items in the sequence // 2
#         midpoint_value = sequence[midpoint]
#         if midpoint_value == item:
#             return midpoint
        
#         elif item < midpoint_value:
#             end_index = midpoint_value - 1

#         # elif item > midpoint_value:
#         else:
#             begin_index = midpoint + 1
#     return None

# sequence_a = [2,4,5,6,7,8,9,12] #must be already sorted
# item_a = 12

# print(binary_search(sequence_a, item_a),"th position")

import sys

n = int(sys.stdin.readline())
s1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
s2 = list(map(int, sys.stdin.readline().split()))




dic = {}
for n in s1:
    try:
        dic[n] += 1
    except:
        dic[n] = 1
result = []
for i in s2:
    try:
        result.append(dic[i])
    except:
        result.append(0)
for i in result:
    print(i, end = ' ')
