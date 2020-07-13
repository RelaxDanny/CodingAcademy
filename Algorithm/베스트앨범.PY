def solution(genres, plays):
    answer = []
    ans_dict = {}
    for each in genres:
        ans_dict[each] = []

    for i in range(len(genres)):
        ans_dict[genres[i]].append((plays[i], i))
        ans_dict[genres[i]].sort(reverse=True)
        
    print(ans_dict)
    # for key, value in ans_dict.items():
    while ans_dict:
        result = max(ans_dict.items())
        if len(result[1]) == 1:
            answer.append(result[1][0][1])
        else:
            answer.append(result[1][0][1])
            answer.append(result[1][1][1])

        if result[0] in ans_dict:
            del ans_dict[result[0]]
    print(ans_dict)
    return answer

print(solution(["classic", "pop", "classic", "classic","pop"], [500,600,150,800,2500]))