N, K = map(int, input().split())

lst = []
ans = 0
for i in range(N):
    lst.append(int(input()))
    

for j in range(1, N + 1):
    if K < lst[-j]:
        continue
    ans += K // lst[-j]
    K = K % lst[-j]
    
print(ans)
