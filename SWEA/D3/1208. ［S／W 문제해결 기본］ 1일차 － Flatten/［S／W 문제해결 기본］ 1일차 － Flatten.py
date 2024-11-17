T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for _ in range(N):
        lst.sort()
        if lst[-1] - lst[0] <= 1:
            break
        lst[-1] -=1
        lst[0] +=1
    ans = max(lst) - min(lst)
    print(f'#{tc} {ans}')