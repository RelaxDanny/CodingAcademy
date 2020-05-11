def solution(numbers, hand):
    Dict = dict()
    answer = ''
    tmp_check = []
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            Dict.setdefault(numbers[i],[]).append("L")
            tmp = str(Dict.get(numbers[i],[-1]))
            
            answer += tmp[-3]

        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            Dict.setdefault(numbers[i],[]).append("R")
            tmp = str(Dict.get(numbers[i],[-1]))
            answer += tmp[-3]

        elif numbers[i] == 2: # check 1, 3, 5
            for j in reversed(range(i)):
                if numbers[j] == 1:
                    for x in reversed(range(j)):
                        if x == 3 or x == 5:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                        break
                if numbers[j] == 3:
                    for x in reversed(range(j)):
                        if x == 1 or x == 5:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                        break
                if numbers[j] == 5:
                    for x in reversed(range(j)):
                        if x == 1 or x == 3:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                        break
                else:
                    if hand == "right": 
                        answer += "R"
                        Dict.setdefault(numbers[i],[]).append("R")
                    elif hand == "left": 
                        answer += "L"
                        Dict.setdefault(numbers[i],[]).append("L")
                    break
                
        elif numbers[i] == 5: # check 2, 4, 6, 8
            for j in reversed(range(i)):
                print("5",Dict)
                if numbers[j] == 2:
                    for x in reversed(range(j)):
                        if x == 4 or x == 6 or x == 8:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                        break
                    break
                if numbers[j] == 4:
                    for x in reversed(range(j)):
                        if x == 2 or x == 6 or x == 8:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                if numbers[j] == 6:
                    for x in reversed(range(j)):
                        if x == 2 or x == 4 or x == 8:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                if numbers[j] == 8:
                    for x in reversed(range(j)):
                        if x == 2 or x == 6 or x == 4:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                    
                        elif x != 2 or x != 6 or x != 4:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                else:
                    if hand == "right": 
                        answer += "R"
                        Dict.setdefault(numbers[i],[]).append("R")
                    elif hand == "left": 
                        answer += "L"
                        Dict.setdefault(numbers[i],[]).append("L")
                    break

        elif numbers[i] == 8: # check 5, 7, 9, 0
            for j in reversed(range(i)):
                if numbers[j] == 5:
                    for x in reversed(range(j)):
                        if x == 7 or x == 9 or x == 0:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                if numbers[j] == 7:
                    for x in reversed(range(j)):
                        if x == 5 or x == 9 or x == 0:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                if numbers[j] == 9:
                    for x in reversed(range(j)):
                        if x == 5 or x == 7 or x == 0:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                if numbers[j] == 0:
                    for x in reversed(range(j)):
                        if x == 7 or x == 9 or x == 5:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                else:
                    if hand == "right": 
                        answer += "R"
                        Dict.setdefault(numbers[i],[]).append("R")
                    elif hand == "left": 
                        answer += "L"
                        Dict.setdefault(numbers[i],[]).append("L")
                    break
        elif numbers[i] == 0: # check 8
            for j in reversed(range(i)):
                if numbers[j] == 8:
                    for x in reversed(range(j)):
                        if x == 8:
                            if hand == "right": 
                                answer += "R"
                                Dict.setdefault(numbers[i],[]).append("R")
                            elif hand == "left": 
                                answer += "L"
                                Dict.setdefault(numbers[i],[]).append("L")
                            break
                        else:
                            tmp = str(Dict.get(numbers[j],""))
                            if tmp != "None":
                                answer += tmp[-3]
                                Dict.setdefault(numbers[i],[]).append(tmp[-3])
                            break
                    break
                else:
                    if hand == "right": 
                        answer += "R"
                        Dict.setdefault(numbers[i],[]).append("R")
                    elif hand == "left": 
                        answer += "L"
                        Dict.setdefault(numbers[i],[]).append("L")
                    break
    print(Dict)
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	
        # "LLRLLRLLRL"
        # "LRRLRRLRRR"

hand = "right"
print(solution(numbers, hand))