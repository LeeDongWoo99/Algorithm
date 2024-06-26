# 카드의 개수와 카드의 합을 입력
N, M = map(int, input().split())
# 각 카드의 숫자를 입력
lst = list(map(int, input().split()))
# 카드의 총 합
result = 0

for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            total = lst[i] + lst[j] + lst[z]
            if total > M:
                continue
            else:
                result = max(result, total)
print(result)
            
            