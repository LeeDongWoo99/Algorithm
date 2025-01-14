import sys
input = sys.stdin.readline

def dfs(depth, start):
	if depth == M:
		print(" ".join(map(str, ans)))
		return

	prev = -1
	for i in range(start, N):
		if prev != arr[i]:
			ans.append(arr[i])
			dfs(depth + 1, i + 1)
			ans.pop()
			prev= arr[i]

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []
dfs (0, 0)