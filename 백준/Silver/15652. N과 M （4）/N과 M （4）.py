import sys
input = sys.stdin.readline

def dfs(depth, i):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    for j in range(i, N + 1):
        arr.append(j)
        dfs(depth + 1, j)
        arr.pop()

N, M = map(int ,input().split())
arr = []

dfs(0, 1)