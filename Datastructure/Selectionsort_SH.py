



def selection_sort(A):
    for i in range(len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
    return A

A = [6,2,4,6,7,8,98,122,1,2,4,6,65]


print(selection_sort(A))


tuple1 = "abcd", 1,2,3,4
lista = [5,4,4,3,6,1]

for each in lista:
    print(each)


for i in range(len(lista)): # 0 1 2 3 4 5
    if lista[2] > lista[3]:
        print("3번째가 4번째보다 더 큽니다.")


# print("loop is done")

# for i in range(5):# i = 0, 1, 2, 3, 4
#     print("ABCDE")
#     print(i)