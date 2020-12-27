#name: jeonghyeon Lee
#Email: jeonghyeon.lee@stonybrook.edu

def threeMostCommonCharacters(word):
    word = word.upper()
    number = {}
    for i in word:
        if i in number:
            number[i] += 1
        else:
            number[i] = 1
    for j in range(0,3):
        count = 0
        key =""
        for i in number:
            if number[i] > count:
                count = number[i]
                key = i

        print(key, ":", count,"", end=" ")
        number[key] = -1

threeMostCommonCharacters("Google")
print()
threeMostCommonCharacters("Mississipi")
print()
threeMostCommonCharacters("Daimlerchrysler")