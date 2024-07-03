import sys
input = sys.stdin.readline

def decimal(n):
    ans = 0
    for i in range(n+1, 2*n + 1):
        if i < 2:  # 2보다 작은 수는 소수가 아님
            continue
        elif i == 2:  # 2는 소수
            ans += 1
            continue
        check = True
        for j in range(2, int(i**0.5) + 1):  # 2는 이미 체크했으므로 홀수만 검사
            if i % j == 0:
                check = False
                break
        if check:
            ans += 1
    return ans

while True:
    n = int(input())
    if n == 0:
        break
    result = decimal(n)
    print(result)

