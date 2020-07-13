from itertools import product
def solution(numbers, target):
    count = 0
    ls = []
    for each in numbers:
        ls.append((each, -each))
    result = list(map(sum, product(*ls)))
    for i in result:
        if target == i:
            count += 1
    return count

print(solution([1,1,1,1,1], 5))


