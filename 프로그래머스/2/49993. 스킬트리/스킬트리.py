def solution(skill, skill_trees):
    result = 0

    for skill_tree in skill_trees:
        skill_index = 0  # 현재 검사해야 할 스킬의 인덱스
        valid = True  # 스킬 트리가 유효한지 여부를 나타내는 플래그

        for s in skill_tree:
            if s in skill:
                if s == skill[skill_index]:  # 올바른 순서로 배우고 있는 경우
                    skill_index += 1
                else:  # 순서가 잘못된 경우
                    valid = False
                    break

        if valid:
            result += 1

    return result