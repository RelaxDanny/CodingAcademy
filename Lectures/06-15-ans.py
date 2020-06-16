def NoC():
    paid = int(input())
    moneyL = [500, 100, 50, 10, 5, 1]
    count = 0
    leftOver = 1000 - paid
    for each in moneyL:
        n = leftOver//each
        if n > 0:
            count += n
            leftOver -= n * each
        elif n == 0:
            pass
    return count
print(NoC())
