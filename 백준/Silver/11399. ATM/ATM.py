n = int(input())
p = list(map(int,input().split()))
p.sort()
s1 = 0
tot = 0
for i in range(n):
    s1 += p[i]
    tot +=s1
print(tot)