import sys
input = sys.stdin.readline

def dfs(depth):
    if depth == M:
        result = tuple(ans)
        if result not in results:
            results.add(result)
            print(*result)
        return

    for i in range(N):
        ans.append(arr[i])
        dfs(depth + 1)
        ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
results = set()

dfs(0)