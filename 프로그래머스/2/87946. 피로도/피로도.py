def solution(k, dungeons):
    max_count = 0
    visited = [False] * len(dungeons)
    
    def dfs(hp, idx, count):
        nonlocal max_count
        if idx == len(dungeons):
            max_count = max(max_count, count)
        
        for i in range(len(dungeons)):
            if hp >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                dfs(hp - dungeons[i][1],idx + 1, count + 1)
                visited[i] = False
        max_count = max(max_count, count)
    dfs(k, 0, 0)
    return max_count
                
    
