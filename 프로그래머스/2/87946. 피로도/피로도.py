def solution(k, dungeons):
    max_ans = 0
    visited = [False] * len(dungeons)
    def dfs(hp, ans):
        nonlocal max_ans
        max_ans = max(max_ans, ans)
        
        for i in range(len(dungeons)):
            if hp >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                dfs(hp - dungeons[i][1], ans + 1)
                visited[i] = False
    dfs(k, 0)
    return max_ans