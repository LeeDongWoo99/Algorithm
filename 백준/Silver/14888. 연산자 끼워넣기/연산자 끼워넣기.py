import sys
input = sys.stdin.readline

max_value = -float('inf')
min_value = float('inf')


def dfs(num, idx):
    global max_value, min_value

    if idx == N:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return

    for i in range(4):
        if operator[i] > 0:
            operator[i] -= 1

            if i == 0:  # 덧셈
                dfs(num + arr[idx], idx + 1)
            elif i == 1:  # 뺄셈
                dfs(num - arr[idx], idx + 1)
            elif i == 2:  # 곱셈
                dfs(num * arr[idx], idx + 1)
            elif i == 3:  # 나눗셈 (정수 나눗셈)
                dfs(int(num / arr[idx]), idx + 1)

            operator[i] += 1


N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

dfs(arr[0], 1)

print(max_value)
print(min_value)