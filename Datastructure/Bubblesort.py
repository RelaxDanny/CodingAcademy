"""
538672 -> 235678
Swapping is the skill for bubble sort

1. compare the first two value
 - if first is greater, swap 5 > 3 => 3 5 8 6 7 2
2. go forward
 - keep doing swap if left is greater
 - 5 3 8 6 7 2
 - 3 5 8 6 7 2
 - 3 5 6 8 7 2
 - 3 5 6 7 8 2
 - 3 5 6 7 8 2
 - 3 5 6 7 2 8
 - 마지막에 biggest가 있게된다. (8 맥시멈이 무조건 마지막에 있게되니 마지막까지 보지는 않는다.)
 - 이걸 반복
 - iteration 1 - 2 - 3 - .. N
 - 3 5 6 7 2 8
 - 3 5 6 2 7 8
 - 3 5 2 6 7 8
 - 3 2 5 6 7 8
 - 2 3 5 6 7 8
 Outer loop = i = 0 to n-1
 Inner loop = j = 0 to n-1-i
2개의 loop을 필요로 함
"""
num = [5,3,8,6,7,2]

def bubblesort(num):
    for i in range(0,len(num)-1):
        for j in range(0, len(num)-1-i):
            if num[j]>num[j+1]:
                num[j], num[j+1] = num[j+1], num[j] #swap
    return num
print(bubblesort(num))