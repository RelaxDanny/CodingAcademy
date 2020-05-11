def solution(gems):
    if(len(set(gems))==1):
        answer = [1,1]
        return answer
        
    answer = []
    tmp = []
    tmp2=[]
    cmp_tmp = []
    result_list = []
    lista = []

    for i in gems:
        cmp_tmp.append(i) 
    set_tmp = set(cmp_tmp)
    list_set = list(set_tmp)
    list_set.sort()    

    for i in range(0, len(gems)-1):
        tmp.append(gems[i])
        for j in range(i+1, len(gems)):
            tmp.append(gems[j])
            tmp2 = set(tmp)
            lista = list(tmp2)
            lista.sort()
            if len(lista) >= len(list_set):
                if lista == list_set:
                    result_list.append(i)
                    result_list.append(j)
                    tmp = []
                else:
                    tmp = []
                break

    listb = []
    for i in range(0, len(result_list), 2):
        listb.append(abs(result_list[i] - result_list[i+1]))

    min_ = min(listb)
    for i in range(0, len(result_list), 2):
        if abs(result_list[i] - result_list[i+1]) == min_:
            answer.append(result_list[i]+1)
            answer.append(result_list[i+1]+1)
    answer = answer[0:2]


    return answer

print(solution(["XYZ", "XYZ", "XYZ"]))