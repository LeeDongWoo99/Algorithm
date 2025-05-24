t = int(input())

for tc in range(1, t + 1):
    n = int(input())  # 대학교에 있어야 하는 일 수
    lst = list(map(int, input().split())) # 수업 시간표
    min_turn = float('inf')

    for start in range(7):
        lesson = 0 # 수업 들은 수
        turn = 0  # 턴 수
        i = start

        while lesson < n:
            if lst[i] == 1:
                lesson += 1
            turn += 1
            i += 1
            i = i % 7
        min_turn = min(min_turn, turn)
    print(f'#{tc} {min_turn}')