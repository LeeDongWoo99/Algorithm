def solution(N, stages):
    
    # 총 플레이어 수
    player = len(stages)
    # 숫자와 실패율을 저장할 튜플
    cal = {}
    # 결과를 담을 리스트
    ans = [ ]

    for i in range(1, N+1):
        if player == 0:
            cal[i] = 0
        else:
            cal[i] = stages.count(i) / player
            player -= stages.count(i)

    ans = sorted(cal, key=lambda x : cal[x], reverse=True)
    return ans
