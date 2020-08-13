def solution(land):
    answer = 0
    reselect = []
    tempLB = []
    tmp = []
    tmp = land

    for eachList in land:
        tempLB.append(eachList)
    # print("L",tempLB)

    for i in range(4):
        x = 0
        tempLB = []

        for eachList in land:
            tempLB.append(eachList)

        for _ in range(i):
            try:
                tempLB[0].remove(max(tempLB[0]))
            except ValueError:
                pass

        # print(str(i)+":", tempLB)

        # print(tempL)
        for each in tempLB:
            try:
                x += max(each)
                tempLB[tempLB.index(each)+1].pop(each.index(max(each)))
                print(tmp)
            except:
                pass
        reselect.append(x)
    # print(reselect)
    answer += max(reselect)
    return answer

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
