letters = '''HI, Yassm sql smwk svk '''

# find = lambda argument : return_value

find = lambda x, y : x[x.find(y)-9:x.find(y)+9] if y in x else -1

print(find(letters, "sql")) #beginning index of the word
# ------------------------------------------------------------------------
price = [[1,2,3,4,5],
        [13,4,5,6,7],
        [14,1,1,2,4],
        [1,2,3,4,1]]
# sample = [expression context]
# line = [1,2,3,4,5]
# line[first: stop: step]
sample = [line[::2] for line in price]
print(sample)
# ------------------------------------------------------------------------

# print(any([True, False, True, False, 0]))
# print(any([1,0,4,0]))

companies = {'ACompany' : {'Alice' : 33, 'Bob' : 28},
             'BCompany' : {'Ann' : 17, 'Lee' : 18}}

# illegal = [expression context]
illegal = [x for x in companies if any()]