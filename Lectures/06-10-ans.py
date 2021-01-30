h = [int(input()) for i in range(9)]
result = sum(h)
h.sort()
for i in range(len(h)):
    for j in range(i+1, len(h)):
        if result - h[i] - h[j] == 100:
            a = h[i]
            b = h[j]
            h.remove(a)
            h.remove(b)
for each in h: print(each)