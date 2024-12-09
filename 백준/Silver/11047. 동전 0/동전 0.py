N, K = map(int, input().split())

lst = []
ans = 0 #K원을 만드는데 필요한 총 동전의 개수
for _ in range(N): # N 크기 만큼 동전 종료 받기
    lst.append(int(input()))


for i in range(1, N+1):
    if lst[-i] > K:
        continue
    ans += K // lst[-i]
    K = K % lst[-i]
    if K == 0:
        break
print(ans)