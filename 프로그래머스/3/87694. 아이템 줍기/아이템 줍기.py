from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 2배 확대된 2D 맵 (최대 좌표값이 50이므로 2배하면 100)
    SIZE = 102
    grid = [[0] * SIZE for _ in range(SIZE)]
    
    # 1. 직사각형을 2배로 확장하고 테두리 표시
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # 내부를 2 (벽), 테두리를 1 (이동 가능)으로 설정
                if x1 < x < x2 and y1 < y < y2:
                    grid[x][y] = 2  # 내부
                elif grid[x][y] != 2:
                    grid[x][y] = 1  # 테두리

    # 2. BFS 탐색 (최단 거리 구하기)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[False] * SIZE for _ in range(SIZE)]
    visited[characterX * 2][characterY * 2] = True
    
    while q:
        x, y, dist = q.popleft()
        
        # 아이템 위치 도착
        if (x, y) == (itemX * 2, itemY * 2):
            return dist // 2  # 원래 크기로 환산
    
        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < SIZE and 0 <= ny < SIZE and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))
