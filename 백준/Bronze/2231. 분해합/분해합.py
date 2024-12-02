N = int(input())
mid_n = int(N / 2)
for M in range(mid_n, N + 1):
    num = sum(map(int, str(M)))
    sum_num = num + M
    if sum_num == N:
        print(M)
        break
    if M == N:
        print(0)

