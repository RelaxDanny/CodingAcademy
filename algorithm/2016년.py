def solution(a, b):
    answer = ''
    cnt = 0
    result = 0
    for i in range(1, a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            cnt = 31
        elif i == 4 or i ==  6 or i == 9 or i == 11:
            cnt = 30
        elif i == 2:
            cnt = 29
        result += cnt
        # print(i)
        
    result += b
    day = result%7
    # print(result)
    if day == 3:
        answer = "SUN"
    if day == 4:
        answer = "MON"
    if day == 5:
        answer = "TUE"
    if day == 6:
        answer = "WED"
    if day == 0:
        answer = "THU"
    if day == 1:
        answer = "FRI"
    if day == 2:
        answer = "SAT"
    return answer

print(solution(11,3))