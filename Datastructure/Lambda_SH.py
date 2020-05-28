"""
람다는 익명 함수이다. 
1. 간결
2. 사람의 언어와 비슷함. 
3. 다른언어에도 존재함.
"""

# list of strings 가정
txt = ["Kim Youngho", "Kim SH", "Lee Youngho", "Ju Youngho"]
# Kim을가진 string을 나열하라.

# prac = [(True, Kim Youngho) , (True, Kim SH), (False, Lee Youngho), (False, Ju Youngho)]

# lambda_prac = map(function , iterables)

prac = map(lambda s: (True, s) if 'Kim' in s else (False, s), txt)
list1= list(prac)
print(list1)
# def x(iterables[i]):
#     return x값
 #def("Kim Youngho"):
    #if "Kim" in "Kim Youngho":
        # return (True, "Kim Youngho")
    #else: return (False, s)

1. 머신러닝 -> 
