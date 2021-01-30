def solution(w,h):
    answer = 1
    if w % 2 == 0:
        w = w - 1
    if h % 2 == 0:
        h = h - 1
    else:
        w = w - 2
        h = h - 2
    tot = 0
    for each in range(h): # h = 5 -> 0,1,2,3,4
        tot += each+1
    print(tot)
    
    

    return answer

print(solution(6,7))