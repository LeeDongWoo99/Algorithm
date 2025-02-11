def solution(k, dungeons):
    max_count = 0
    def dfs(hp, count):
        nonlocal max_count
        max_count = max(max_count, count)
    
        for i in range(len(dungeons)):
            if hp >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                dfs(hp - dungeons[i][1], count + 1)
                visited[i] = False
    visited = [False] * len(dungeons)
    dfs(k, 0)
    return max_count