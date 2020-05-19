"""

5! = 5 x 4 x 3 x 2 x 1 = 120

0! = 1
1! = 1

Recursion => Iterative Algorithm [Loop]
- Use loops and compute as it goes 

Psuedocode:

function getFactorial(5)
    factorial = 1
    for x = 1 to 5
        factorial = factorial * x

5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1
0! = 1

fun(5) = 5 * fun(4)
fun(4) = 4 * fun(3)
fun(3) = 3 * fun(2)
fun(2) = 2 * fun(1)
fun(1) = 1
fun(0) = 1

Why recursion?
    - 100,000,000! = 100,000,000 * 99,999,999! ?? 값이 커질수록 recursion은 느려진다.
    - Binary Search, Binary tree Algorithm recursion 을 사용. 

Recursion 특징:

    단점: 
    1. for loop사실 더 빠름
    2. function을 무조건 사용해야해서 느림
    3. 값이 커질수록 계산이 너무 오래걸림.
    4. 타인이 보기 어려워함.

    장점:
    1. binary search, tree search 같은 데이터 구조에선 더욱 빠르게 작용함. 
    2. 겉멋. 

"""
def getFactorial(n):
    if n < 2: return 1 #when 0 or 1
    else: return n * getFactorial(n-1)
print(getFactorial(5))

import math

print(math.factorial(100000))