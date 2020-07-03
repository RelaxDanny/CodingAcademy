def solution(participant, completion):
    dict = {}
    for each in participant:
        if each in dict:
            dict[each] += 1
        else:
            dict[each] = 1     
    for each in completion:
        if each in dict:
            dict[each] -= 1
        else:
            dict[each] += 1  
    print(dict)
    for key, val in dict.items():
        if val == 1:
            return key


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))