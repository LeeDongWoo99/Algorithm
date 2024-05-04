dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] *N for _ in range(N)]
    
    # 초기화
    x, y, cnt, dr = 0, 0, 1, 0
    snail[x][y] = cnt
    cnt+=1

    while cnt <= N * N:
        nx, ny = x + dx[dr],  y + dy[dr]
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            x, y = nx, ny
            snail[x][y] = cnt
            cnt+=1
        else:
            dr = (dr +1) % 4
    
    print(f'#{test_case}')
    for row in snail:
        print(*row)