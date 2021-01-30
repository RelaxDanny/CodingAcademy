"""
5! = Five factorial = 1*2*3*4*5 = 120

Notes : 0! = 1
      : 1! = 1

An Iterative Algorithm

- useing loop and computes as it goes.

function getFactorial(5)
    factorial = 1
    for x = 1 to 5
        factorial = factorial * x

Why recursion?
 - it breask the problem down into smaller problems, and calls itself for each of the smaller problems.

5! = 5 * 4!
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1
0! = 1

Funtion calls:
getFactorial(5)     #5*getFactorial(4)                  =120 -> return to the original function call
    getFactorial(4)     #4*getFactorial(3)              =24
        getFactorial(3)     #3*getFactorial(2)          =6
            getFactorial(2)     #2*getFactorial(1)      =2
                getFactorial(1)     return 1            =1

recursion은 무조건 끝까지 가야 해답이 나오기 때문에 1,000,000! 같은걸 돌렸다간 몇년걸림, 상대가 알아보기 힘듬, 
사실 for loop이 왠만하면 더 빠름(function 생성안해도 돼서)
하지만, binary search, tree search 같은 데이터 구조에선 더욱 빠르게 작용함

"""
def getFactorial(n):
    if n < 2: return 1
    else: return n*getFactorial(n-1)

print(getFactorial(5))