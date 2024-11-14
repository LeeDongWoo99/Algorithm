def dfs(index, score, calorie):
    global max_score
    if calorie > K:
        return
    if index == N:
        max_score = max(max_score, score)
        return
    # 재료를 선택했을 때
    dfs(index + 1, score + lst[index][0], calorie + lst[index][1])
    # 재료를 선택하지 않았을 때
    dfs(index + 1, score, calorie)


T = int(input())
for tc in range(1, T+1):
    # 재료수와 제한된 칼로리
    N, K = map(int, input().split())
    # 맛 점수와 칼로리량
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    dfs(0, 0, 0)
    print(f'#{tc} {max_score}')