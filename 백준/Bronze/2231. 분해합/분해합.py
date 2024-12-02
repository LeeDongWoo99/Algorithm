N = int(input())
mid_n = int(N / 2)
for M in range(mid_n, N):
    ans = 0
    str_n = str(M)
    for i in str_n:
        ans += int(i)
    if ans + M == N:
        print(M)
        break
else:
    print(0)


