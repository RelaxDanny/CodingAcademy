def solution(arrangement):
    answer = 0
    arrangement = list(arrangement)
    s = 0
    while len(arrangement) != 0:
        if arrangement[0] == "(":
            s += 1
            arrangement.pop(0)
            if arrangement[0] == ")":
                s -= 1
                answer += s
                arrangement.pop(0)
        else:
            arrangement.pop(0)
            s -= 1
            answer += 1
    
    return answer