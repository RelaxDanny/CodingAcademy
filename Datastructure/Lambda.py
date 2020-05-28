"""
list of string이 있다고가정

boolean 을 활용하여 kim이 있는걸 찾아보기

"""

txt = ['hi youngho Kim.', 'hi SH.', 'hi Kim.']

mark = map(lambda s: (True, s) if 'Kim' in s else (False, s), txt)
#여기서 s는 txt list의 각각의 스트링을 의미한다. 
#imply the function to each iterables
#map은 2개의 arg을 받는데 fucntion과 iterable을 받는다
# output = [(True, 'lamda function...'), True, 'anonyom...'), (Fales, 'functions...)]
# 2 + 2 if 2 > 0 else 3 + 3 이런식으로 적는게 람다 형식 -> 매우 말에 가까운 코드

print(list(mark))