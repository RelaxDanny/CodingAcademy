num1 = float(input('give me a number: '))
num2 = float(input('give me second number: '))
num3 = float(input('give me third number: '))
num4 = float(input('give me fourth number: '))

print('q=arithmetic mean, w=geometric mean e=(num1 - num2) * num3 / num4')

choice = input("Enter choice(q/w/e): ")

import math
if choice == 'q':
    print((num1 + num2)/2)
elif choice == 'w':
    print(math.sqrt(num1 * num2) )
elif choice == 'e':
    print( (num1 - num2) * num3 / num4 )2