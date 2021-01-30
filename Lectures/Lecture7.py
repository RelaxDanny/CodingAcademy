
# 1 ~ 10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하세요.
total = 0
for num in range(11):
    total = total + num
print(total)

# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 해당 숫자에 대한 구구단을 출력하세요.
digit = input()#always str
for num in range(1,10):
    result = int(digit) * num
    print(digit, "x", num, "=", result)


#1부터 30까지의 숫자 중 3의 배수만 출력하세요.
for num in range(1, 31):
    if num % 3 == 0:
        print(num)