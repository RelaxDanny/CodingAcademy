"""
왜배우나?
1. 타인이 쓴걸 쉽게 이해하기위해 
 - 파이썬을 잘 쓰는사람들은 원라인으로 표현을 잘한다.
 - 아는만큼 보인다!
"""

#Find the top employee! 
employees = {'Alice' : 100000,
             'Bob' : 99817,
             'Carol' : 122908,
             'Frank' : 88123,
             'Eve' : 93121}

top_earners = []
for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key, val))
print(top_earners)


#List comprehension
# lst = [1,2,3,4,5,6 ... ]
# lst = [expression context]
lst = [x for x in range(10)] # lst라는 리스트 안에 긴 값을 저장!
#0 1 2 3 4 5 6 7 8 9 
lst = [x + x for x in range(10)] 
#0 2 4 6 8 10 12 14 16 18
lst = [x**2 for x in range(10)]
#0 1 4 9 16 25 36 49 64 81

top_earners = [(key, val) for key, val in employees.items() if val >= 100000 if key == 'Alice']
print(top_earners)

#--------------------------------------#--------------------------------------#--------------------------------------

# #Read file and Strip lines
# filename = "Datastructure/OneLiner.py"
# f = open(filename, 'rt', encoding='UTF8')
# lines = []
# for line in f:
#     lines.append(line.strip())
# print(lines)
# #strip 예시 보여주기
# lst2 = [line.strip() for line in open("Datastructure/OneLiner.py")]

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    else: return fib(n-1) + fib(n-2) 
print(fib(10))



