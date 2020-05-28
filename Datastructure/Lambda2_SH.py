
# find = lambda argument : return value

# def find(x,y):
#     if x != 0:
#         return x+y
#함수
find = lambda x, y : x + y if x != 0 else 0

print(find(1,5))

twoDarr = [[1,2,3,4,5],
           [2,3,4,5,6],
           [3,4,5,6,7],
           [4,5,6,7,8]]

# print(twoDarr[1::2])

# sample = [expression context]
sample = [line[1::2] for line in twoDarr]

#One Line OR Lambda


# for line in twoDarr:
#     sample.append(line[1::2])

# slice
list1 = [1,2,3,4,5]
print(list1[0:6:2]) # : ~부터 ~ 전까지 SLICE
#list[first index : end index: step]