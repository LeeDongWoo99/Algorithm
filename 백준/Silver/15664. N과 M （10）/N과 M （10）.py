import sys
input = sys.stdin.readline

def dfs(start):
    if len(ans) == M:
        print(*ans)
        return

    prev = -1
    for i in range(start, N):
        if not visited[i] and arr[i] != prev:
            visited[i] = True
            ans.append(arr[i])
            prev = arr[i]
            dfs(i + 1)
            visited[i] = False
            ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [False] * N

dfs(0)