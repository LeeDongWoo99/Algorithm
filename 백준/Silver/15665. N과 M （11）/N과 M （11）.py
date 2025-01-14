import sys
input = sys.stdin.readline

def dfs(depth):
    if depth == M:
        print(*ans)
        return

    prev = -1
    for i in range(N):
        if prev != arr[i]:
            ans.append(arr[i])
            dfs(depth + 1)
            ans.pop()
            prev = arr[i]


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

dfs(0)