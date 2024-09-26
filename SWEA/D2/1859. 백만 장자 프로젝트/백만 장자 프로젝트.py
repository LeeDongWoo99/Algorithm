T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    ls = list(map(int, input().split()))
    mp = 0
    ans = 0
    for val in ls[::-1]:
        if val >= mp:
            mp = val
        else:
            ans += mp - val
    print(f'#{tc} {ans}')