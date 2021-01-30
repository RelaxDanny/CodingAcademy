word = input()
listA = []
listB = []
listC = []
for i in range(len(word)):
    for j in range(i+1, len(word)):
        listA.append(word[i:j])

rev_listA = []
print(listA)
for i in range(len(word)):
    rev_listA.append(listA[-1])