from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 1)])  # (x, y, distance)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 목적지에 도달했을 때 거리 반환
        if x == n - 1 and y == m - 1:
            return distance
        
        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    
    return -1

def solution(maps):
    return bfs(maps)
