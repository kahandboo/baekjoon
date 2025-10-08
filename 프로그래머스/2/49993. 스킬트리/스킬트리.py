def solution(skill, skill_trees):
    answer = 0
    skill_dict = {s:0 for s in skill}

    for skill_tree in skill_trees:
        i = 0
        j = 0
        while i < len(skill_tree):
            if skill_tree[i] in skill_dict:
                if skill[j] != skill_tree[i]:
                    break
                else:
                    j += 1
            i += 1
        else:
            answer += 1
            
    return answer