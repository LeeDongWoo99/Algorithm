from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    board[x][y] = 2  # 내부 부분은 2로 마킹 (탐색 X)
                elif board[x][y] != 2: 
                    board[x][y] = 1  # 테두리는 1로 마킹 (탐색 가능)
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = True  # ✅ 오타 수정

    while q:
        x, y, dist = q.popleft()
        
        if (x, y) == (itemX * 2, itemY * 2):  # 목적지 도착
            return dist // 2  # 2배 했으므로 거리도 절반으로 변환
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True  # ✅ 문법 오류 수정 (":" 제거)
                q.append((nx, ny, dist + 1))
