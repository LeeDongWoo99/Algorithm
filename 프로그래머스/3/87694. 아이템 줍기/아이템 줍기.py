from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 102
    grid = [[0] * SIZE for _ in range(SIZE)]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    grid[x][y] = 2  # 내부
                elif grid[x][y] != 2:
                    grid[x][y] = 1  # 테두리

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[False] * SIZE for _ in range(SIZE)]
    visited[characterX * 2][characterY * 2] = True
    
    while q:
        x, y, dist = q.popleft()
        
        if (x, y) == (itemX * 2, itemY * 2):
            return dist // 2 
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < SIZE and 0 <= ny < SIZE and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
