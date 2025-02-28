import sys
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())

if k > c* r:
    print(0)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

lst = [[0] * c for _ in range(r)]
x, y = 0, 0
dir = 0

person = 1
cnt = 1

for person in range(1, c * r + 1):
    if k == person:
        print(y + 1, x + 1)
        break
    else:
        lst[x][y] = k

        x += dx[dir]
        y += dy[dir]

        if x < 0 or y < 0 or x >= r or y >= c or lst[x][y]:
            x -= dx[dir]
            y -= dy[dir]

            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]
    



