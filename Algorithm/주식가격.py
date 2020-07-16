def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        flag = False
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                flag = True
                break
        if flag == False:
            answer.append(len(prices)-i-1)
    answer.append(0)

    return answer