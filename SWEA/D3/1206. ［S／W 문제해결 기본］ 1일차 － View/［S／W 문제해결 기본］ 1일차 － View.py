T = 10

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    for i in range(2, len(lst) - 2):
        max_a = max(lst[i - 1], lst[i - 2], lst[i + 1], lst[i + 2])

        if lst[i] > max_a:
            ans += lst[i] - max_a


    print(f'#{tc} {ans}')


