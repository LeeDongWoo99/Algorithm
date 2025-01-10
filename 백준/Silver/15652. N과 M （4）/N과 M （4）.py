import sys
input = sys.stdin.readline

def dfs(depth, start):
    if (depth == M):
        print(" ".join(map(str, arr)))
        return

    for i in range(start, N + 1):
        arr.append(i)
        dfs(depth +1, i)
        arr.pop()


N, M = map(int, input().split())
arr = []
dfs(0, 1)