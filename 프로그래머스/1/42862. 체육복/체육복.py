def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reverse_set = set(reserve) - set(lost)
    
    for r in sorted(reverse_set):
        if r - 1 in  lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:  # 뒷번호 학생에게 빌려줌
            lost_set.remove(r + 1)
    
    # 전체 학생 수 - 체육복을 못 빌린 학생 수
    return n - len(lost_set)