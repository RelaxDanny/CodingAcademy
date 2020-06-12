"""
(! (CHILD x)) (LOVES x s)
(! (LOVES x s)) (! (REINDEER y)) (LOVES x y)
(REINDEER r)
(REDNOSE r)
(! (REDNOSE x)) (WEIRD x) (CLOWN x)
(! (REINDEER x)) (! (CLOWN x))
(! (WEIRD x)) (! (LOVES s x))
(! (CHILD s))

"""

data = open("./Datastructure/santa.txt", "r")
# data = open("howling-hounds.txt", "r")
lineByLine = [each.strip() for each in data.readlines()]
variable_list = ['u','v','w','x','y','z']

# print the given facts
line_num = 1
print('---------- GIVEN FACTS ----------')
for fact in lineByLine:
    print(str(line_num) + '. ' + fact)
    line_num += 1
print('---------------------------------\n')
print("Negate the last fact to prove the theorem.")

# negate the last fact
if '!' in lineByLine[-1]:
    lineByLine[-1] = fact[3:-1]
else:
    lineByLine[-1] = '(! ' + fact + ')'

# print the altered facts
line_num = 1
#result_txt contains the final result. It will be updated as new resolution has been found
result_txt = []
print('\n---------- START PROVING ----------')
for fact in lineByLine:
    print(str(line_num) + '. ' + fact)
    result_txt.append(fact) #
    line_num += 1
print('---------------------------------\n')



# save given facts to sentence_list line by line
def data_cleansing(lineByLine):
    sentence_list = []
    sentence_dict = {}
    tmp = []

    for i in range(len(lineByLine)):
        sentence_list.append(lineByLine[i].split(") "))
        
    #Create a dictionary
    #sentence_dict = { Number : [negation = 1 , # of variable, predicate],[...]}
    for x in reversed(sentence_list):
        #from reversed for loop, if ) is seen, exit and remove the unnecessary part
        if ")" == x:
            sentence_list.remove(sentence_list[sentence_list.index(x)+1:])
            pass
    print(sentence_list)

    for i in range(len(sentence_list)):
        tmp = []
        for j in range(len(sentence_list[i])):
            tmp2 = []
            var_counter = 0
            if "!" in sentence_list[i][j]:
                tmp2.append(1)
            elif "!" not in sentence_list[i][j]:
                tmp2.append(-1)
            for each in sentence_list[i][j]:
                if ord(each) >= 96 and ord(each) <=122:
                    var_counter += 1
            tmp2.append(var_counter)
            if "!" in sentence_list[i][j] and sentence_list[i][j][-2] != ")":
                tmp2.append(sentence_list[i][j]+") ")
            elif sentence_list[i][j][-1] != ")":
                tmp2.append(sentence_list[i][j]+") ")
            else:
                tmp2.append(sentence_list[i][j])
            tmp.append(tmp2)
            sentence_dict[i+1] = tmp
    return sentence_dict


#BFS Search Approach
"""
1. 1번 딕셔너리 부터 모든 딕셔너리를 돌면서 본인과 var이 같고, negation이 
다른 clause를 찾는다.

2. 만약 찾으면 딕셔너리에 새로운 Number : [negation, var, predicate] 를 추가한다.
    - 여기서 predicate는 기존의 clause와 pair인 clause를 

3. 현재까지 나온 딕셔너리에서 !Predicate = Predicate형식의 데이터를 찾는다.
# """
def do_resolution(sentence_dict):
    for i in range(1, len(lineByLine)+1):
        for x in range(len(sentence_dict[i])):
            for j in range(i+1, len(lineByLine)+1):
                #if negation is different, num of var is same, and predicates are same => resolution
                    for c in range(len(sentence_dict[j])):
                        predicate_i = ""
                        predicate_j = ""
                        var_i = ""
                        var_j =""
                        final_resol_i = ""
                        final_resol_j = ""
                        resol = ""
                        for value in sentence_dict[i][x][2]:
                            if ord(value) >= 65 and ord(value) <=90:
                                predicate_i += value
                            # elif value == 'u' or value == 'v'or value == 'w'or value == 'x' or value == 'y' or value == 'z':
                                # var_i += value
                            elif ord(value) >= 96 and ord(value) <=122:
                                var_i += value
                        for value in sentence_dict[j][c][2]:
                            #var / constant
                            # if value
                            if ord(value) >= 65 and ord(value) <=90:
                                predicate_j += value
                            # elif value == 'u' or value == 'v'or value == 'w'or value == 'x' or value == 'y' or value == 'z':
                            #     var_j += value
                            elif ord(value) >= 96 and ord(value) <=122:
                                var_j += value
                        
                        if predicate_i == predicate_j and sentence_dict[i][x][0] != sentence_dict[j][c][0] and sentence_dict[i][x][1] == sentence_dict[j][c][1]:
                            #compare the length of each values and remove the predicate of the greater key.
                            # print(sentence_dict[i][x])

                            for k in range(len(sentence_dict[i])):
                                # print("K: ",k)
                                if k != x:
                                    final_resol_i += sentence_dict[i][k][2]
                                    # print("I: ",final_resol_i)
                            for g in range(len(sentence_dict[j])):
                                # print("G:",g)
                                if g != c:
                                    final_resol_j += sentence_dict[j][g][2]
                                    # print("J: ",final_resol_j)
                            resol = final_resol_i + final_resol_j
                            
                            addition = ""

                            for varNum in range(len(var_i)):
                                #pass if same
                                if var_i[varNum] == var_j[varNum]:
                                    pass

                                elif var_i[varNum] in variable_list and var_j[varNum] in variable_list:
                                    addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                    resol = resol.replace(var_i[varNum], var_j[varNum])
                                    
                                elif var_i[varNum] in variable_list and var_j[varNum] not in variable_list:
                                    addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                    resol = resol.replace(var_i[varNum], var_j[varNum])

                                elif var_i[varNum] not in variable_list and var_j[varNum] in variable_list:
                                    addition += ", "+var_j[varNum]+"/"+var_i[varNum]
                                    resol = resol.replace(var_j[varNum], var_i[varNum])

                                elif var_i[varNum] not in variable_list and var_j[varNum] not in variable_list:
                                    addition += ", "+var_i[varNum]+"/"+var_j[varNum]
                                    resol = resol.replace(var_i[varNum], var_j[varNum])

                            resol_result = (resol+", "+str(i)+" & "+str(j)) + addition
                            result_txt.append(resol_result)
                            # print(resol_result)    
    # print result
    for n in range(len(result_txt)):
        print(str(n+1)+". "+result_txt[n])      

#dictionary contains the cleansed data.
dictionary = data_cleansing(lineByLine)                 
do_resolution(dictionary)


#DFS Search Approach