def coin(Type, cost):
    ways = 0
    n = []
    for each in range(Type):
        x = int(input())
        n.append(x)
    n.sort()
    n.reverse()
    if 1 <= Type <= 10:
        for i in range(len(n)):
            if cost//n[i] > 0:
                a = cost//n[i]
                ways += a
                cost -= a*n[i]
        return ways
m, n = map(int, input().split())
print(coin(m, n))