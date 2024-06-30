def solution(k, dungeons):
    max_dungeons = 0
    
    def dfs(current_k, visited, count):
        nonlocal max_dungeons
        max_dungeons = max(max_dungeons, count)
        
        for i in range(len(dungeons)):
            if not visited[i] and current_k >= dungeons[i][0]:
                visited[i] = True
                dfs(current_k - dungeons[i][1], visited, count + 1)
                visited[i] = False
    visited = [False] * len(dungeons)
    dfs(k, visited, 0)

    return max_dungeons