def solution(n, lost, reserve):
    answer = 0
    tmp = [i+1 for i in range(n)]
    tmp_zero = [1 for _ in range(n)]
    for i in range(len(lost)):
        for j in range(len(tmp)):
            if lost[i] == tmp[j]:
                tmp_zero[tmp.index(lost[i])] -= 1

    for i in range(len(reserve)):
        for j in range(len(tmp)):
            if reserve[i] == tmp[j]:
                tmp_zero[tmp.index(reserve[i])] += 1

    answer = tmp_zero
    for i in range(len(answer)):
        if answer[i] == 2 and answer[i] == 2 :
            if i >= 1:
                if answer[i-1] == 0 and answer[i] == 2:
                    # print(answer)
                    answer[i] -= 1
                    answer[i-1] += 1
            if i < len(answer)-1 and answer[i]==2:
                if answer[i+1] == 0:
                    answer[i] -= 1kyj
                    answer[i+1] += 1
    print(answer)
    result = 0
    for i in range(len(answer)):
        if answer[i] != 0:
            result += 1
    return result

print(solution(3, [1,2], [2,3])) 
