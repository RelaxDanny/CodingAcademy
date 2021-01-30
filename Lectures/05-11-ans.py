
# 우리는 주어진 pip들을 보고 주사위를 최적의 방법으로 모두 같은 숫자로 맞춰야 한다. 

# 주사위에는 1 부터 6까지의 pips가 있다.

# pip은 주사위의 점을 말하며 각 pip들은 다음과 같은 성질을 가지고 있다.

# pip의 1, 6
# pip의 2, 5
# pip의 3, 4 는 모두 서로 마주고보고 있는 면이고, 절대 양옆에 서로가 있을 수 없다.

# 예를 들어, 주사위의 윗면이 1이라고 할때, 주사위의 왼쪽, 오른쪽, 또는 가로, 세로 모두 6이 나올 수 없다.

# 주사위를 단 한칸만 뒤집을 수 있을 때, 주사위의 pip이 1이라면 한칸의 움직임으로 주사위는 2,3,4,5를 표현할 수 있다.
# 하지만 6을 표현하기 위해서는 서로 마주보고 있기에 한 번의 움직임으로 표현 할 수 없다.


# [1, 1, 3]이 입력으로 주어졌다고 가정하자.
# 1을 3으로 만들기 위해서 주사위를 한 번만 뒤집으면 되니 이 방법은 1을 소모하고, 
# 두번째 1도 3으로 만들기 위해서는 한 번만 뒤집으면 되닌 1을 추가로 소모해,
# [3,3,3]을 만들기 위해 총 2번의 움직임이 발생했다. 하지만, 주어진 입력 주사위 pip 리스트를
# [1,1,1]로 바꾼다고 가정하였을때, 우리는 3에 대해서 한 번의 움직임으로 모든 주사위의 pip이 같아졌으므로 이 입력에 대한
# 최적의 정답은 바로 1이 된다.

# [1, 1, 3, 4] = 2
# [1, 6, 1, 6] = 4

# 리스트의 최대 개수는 1 < N < 100이며 각 pip은 6을 넘지 않는다.

def solution(A):
    count = 0
    count_list = []
    for i in range(len(A)):
        count = 0
        for j in range(0, len(A)):
            if i != j:
                if A[i] == 1 and A[j] == 6:
                    count += 2
                elif A[i] == 2 and A[j] == 5:
                    count += 2
                elif A[i] == 3 and A[j] == 4:
                    count += 2
                elif A[i] == 4 and A[j] == 3:
                    count += 2
                elif A[i] == 5 and A[j] == 2:
                    count += 2
                elif A[i] == 6 and A[j] == 1:
                    count += 2
                elif A[i] == A[j] and A[j] == A[i]:
                    count += 0
                elif A[i] != A[j] and A[j] != A[i]:  
                    count += 1
            else:
                pass
        count_list.append(count)
    return min(count_list)



import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])

#or 
v = [tuple(map(int,input().split())) for _ in range(int(input()))] # 입력
v = sorted(v, key = lambda x:(x[0],x[1])) # sorting
for i in v : print(i[0], i[1]) # 출력

