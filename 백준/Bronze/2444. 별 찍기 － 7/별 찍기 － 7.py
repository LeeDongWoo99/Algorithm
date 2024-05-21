# 마름모 변 입력받기
n = int(input())
N = 2 * n - 1
ans = 1
cnt = 1
while ans < n + 1:
    if cnt < n + 1:
        print(" " * (n - cnt) + "*" * (2 * cnt - 1))
        cnt += 1
    else:
        print(" " * ans + "*" * (2 * n - 2 * ans - 1))
        ans += 1
