
# From a list containing ints, strings and floats, make three lists to store them separately
# Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
 

# 2개의 리스트 먼저 선언
# for 룹으로 1 부터 101까지 each 만들어주기
# 각 loop 마다 odd 인지, even 넘버 인지 if 문 작성하기
# 프린트 하기


oddList = []
evenList = []
#variable은 항상 소문자로 시작!!! odd list -> oddList, even list -> evenList => Camel writing 

for each in range(1,101):
    if each % 2 == 0:#for even nums
        evenList.append(each)
    elif each % 2 == 1:
        oddList.append(each)

print(oddList, evenList)