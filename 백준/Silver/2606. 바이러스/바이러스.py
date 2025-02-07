from collections import deque

computer = int(input())
v = int(input())
graph = [[] for _ in range(computer + 1)]
virus = [0] * (computer + 1)

for _ in range(v):
    com1, com2 = map(int, input().split())
    graph[com1] += [com2]
    graph[com2] += [com1]

virus[1] = 1
Q = deque([1])

while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if virus[nx] == 0:
            Q.append(nx)
            virus[nx] = 1
print(sum(virus) - 1) # 1에 의해 바이러스가 걸린 컴퓨터의 수이기 때문에 1을 제외해야 한다.