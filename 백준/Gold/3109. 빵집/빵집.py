import sys
input = sys.stdin.readline
ans = 0

def dfs(x, y):
    if y == C - 1:
        return True

    for dx in (-1, 0, 1):
        nx = dx + x
        ny = y + 1

        if 0 <= nx < R and 0 <= ny < C:
            if road[nx][ny] != "x" and visited[nx][ny] == -1:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False

R, C = map(int, input().split()) # 길의 가로 세로 크기 입력
road = [list(input().strip()) for _ in range(R)] # 길의 빈칸과 건물 입력
visited = [[-1 for _ in range(C)] for _ in range(R)]

for i in range(R):
    if dfs(i, 0):
        ans += 1
print(ans)