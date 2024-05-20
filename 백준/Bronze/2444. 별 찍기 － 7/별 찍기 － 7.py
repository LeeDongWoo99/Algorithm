# 마름모 변 입력받기
n = int(input())
N = 2 * n - 1
for i in range(0, n):
    print(" " * (n - i - 1) + "*" * ((2 * i) + 1))
for j in range(1, n):
    print(" " * j + "*" * (N - (2 * j)))
