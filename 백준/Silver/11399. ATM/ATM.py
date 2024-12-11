N = int(input())
P = list(map(int, input().split()))

P.sort()

ans = 0
tot = 0
for i in P:
    tot = i + tot
    ans += tot

print(ans)
