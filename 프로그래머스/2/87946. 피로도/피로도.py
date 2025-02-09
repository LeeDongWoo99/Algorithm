def dfs(hp, idx, ans, dungeons):  # dungeons를 매개변수로 전달
    global max_ans
    if idx == len(dungeons):
        max_ans = max(max_ans, ans)
        return

    for i in range(len(dungeons)):
        if hp >= dungeons[i][0] and not visited[i]:  # visited[i] == False 대신 not 사용
            visited[i] = True
            dfs(hp - dungeons[i][1], idx + 1, ans + 1, dungeons)
            visited[i] = False
        else:
            dfs(hp, idx + 1, ans, dungeons)

def solution(k, dungeons):
    global max_ans
    max_ans = 0
    global visited
    visited = [False] * len(dungeons)  # 리스트 초기화 오류 수정
    dfs(k, 0, 0, dungeons)  # dungeons를 매개변수로 전달
    return max_ans