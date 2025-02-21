def solution(n, lost, reserve):
    # 여벌을 가지고 있지만 도난당한 학생을 먼저 제외
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    # 체육복 빌려주기
    for r in sorted(reserve_set):  # 정렬하여 작은 번호부터 빌려줌
        if r - 1 in lost_set:  # 앞번호 학생에게 빌려줌
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:  # 뒷번호 학생에게 빌려줌
            lost_set.remove(r + 1)
    
    # 전체 학생 수 - 체육복을 못 빌린 학생 수
    return n - len(lost_set)
