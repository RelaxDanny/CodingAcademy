
def solution(user_id, banned_id):
    answer = 0
    banned_tok = []
    user_tok = []
    tot = []
    tot_tok = []
    answer_list = []
    for i in range(len(banned_id)): #0~1
        for j in range(len(user_id)):#0~4
            #1. 길이가 일단 같은걸 찾기     
            if len(banned_id[i]) == len(user_id[j]): #그 선택한 user_id값과 banned_id를 비교
                #2. 스트링을 캐릭터로 펼치기
                for tok in banned_id[i]:
                    banned_tok.append(tok)
                #3. banned_tok랑 user_tok비교하기
                for tok in user_id[j]:
                    user_tok.append(tok)
                    count = 0
                    for x in banned_tok:
                        if x in user_tok:
                            count += 1
                        if count > 2:
                            tot.append(user_id[j])
                        tot = list(dict.fromkeys(tot))
                # for z in range(len(tot)):
                #     for tok in tot[z]:
                #         tot_tok.append(tok)
                # for tok in banned_id[i]:
                #     if tok in tot_tok:
                #         count += 1
                #         if count > 2:
                #             answer_list.append(tot[z])
                banned_tok = []
                user_tok = []
    
    print(tot)
  
    return answer


a=["frodo", "fradi", "crodo", "abc123", "frodoc"]
b=["fr*d*", "*rodo", "******", "******"]
print(solution(a,b))