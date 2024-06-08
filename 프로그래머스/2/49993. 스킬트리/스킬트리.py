def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        check_list = []
        for sk in skill_tree:
            if sk in skill:
                check_list.append(sk)
                
        is_valid = True
        for i in range(len(check_list)):
            if check_list[i] != skill[i]:
                is_valid = False
                break
        if is_valid:
            result +=1

    return result