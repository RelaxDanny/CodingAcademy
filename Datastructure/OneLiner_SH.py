"""
OneLiner !! 

!! 파이썬의 최고장점 다른언어에서는 거의 불가능한 장점!

왜배우는지?
1. oneliner로 된 오픈소스가 70%
2. 아는만큼 보인다!
3. 파이썬을 잘하는 사람은 대부분 one line을 선호한다 간결함!
"""
employees = {'Alice' : 100000,
             'Bob' : 99999,
             'Carol' : 122908,
             'SH' : 12112111,
             'Youngho' : 2}

#최고 연봉자를 찾으세요.

top_earners = []
for k, v in employees.items():
    if v >= 1000000:
        top_earners.append((k, v))
print(top_earners)


top_earners = [(k, v) for k, v in employees.items()]
print(top_earners)
# [('Alice', 100000), ('Bob', 99999), ('Carol', 122908), ('SH', 12112111), ('Youngho', 2)]
top_earners = [(k, v) for k, v in employees.items() if v >= 1000000]
print(top_earners)
# [('SH', 12112111)]
top_earners = [(k, v) for k, v in employees.items() if v >= 1000000 if k == 'SH']
print(top_earners)

for k,v in employees.items():
    if v >= 1000000:
        if k == 'SH':
            top_earners.append((k,v))

#List Comprehension
lst = [1,2,3,4,5,6]
# lst = [1,2,3,4,5, ..., x]

# lst = [expression context]

lst = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [x+x+x for x in range(10)]
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
lst = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
lst = [x**2 for x in range(10) if x == 5 or x == 6]
# [25, 36]
print(lst)