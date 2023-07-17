import sys
input = sys.stdin.readline

n, k = map(int,input().split())
n1 = list(map(int,input().split()))

ls = []
ls.append(sum(n1[:k]))

for i in range(n-k):
    ls.append(ls[i] - n1[i] + n1[i+k])

print(max(ls))