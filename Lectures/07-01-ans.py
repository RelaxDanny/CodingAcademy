# 스킬트리 문제
def solution(skill, skill_trees):
    answer = 0
    for each in skill_trees:
        skill_spell = ""
        for spell in each:
            if spell in skill:
                skill_spell += spell
        if skill_spell == skill[0:len(skill_spell)]:
            answer+=1
    return answer

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "AEB"]))


axis = [(0,0),(0,1),(0,2)]
x, y = axis.pop(0)

print(x,y, axis)