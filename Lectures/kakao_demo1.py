from collections import Counter



def solution(v):
    answer = []
    tmp_x = []
    tmp_y = []
    for i in range(len(v)):
        tmp_x.append(v[i][0])
        tmp_y.append(v[i][1])
    #find the most frequent points
    result_x = Counter(tmp_x).most_common(1)[0][0]
    result_y = Counter(tmp_y).most_common(1)[0][0]
    #remove the duplicates of each x and y variable
    tmp_x = list(dict.fromkeys(tmp_x))
    tmp_y = list(dict.fromkeys(tmp_y))
    #remove the most frequented point from the list
    tmp_x.remove(result_x)
    tmp_y.remove(result_y)
    #the remainders are the x and y values
    answer.append(tmp_x[0])
    answer.append(tmp_y[0])
    return answer

x = [[1, 1], [2, 2], [1, 2]]

print(solution(x))