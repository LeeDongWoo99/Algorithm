N = int(input())
result = 0
for i in range(1,N+1):
    A = list(map(int, str(i)))
    result = sum(A) + i
    if result == N:
        print(i)
        break
    if N == i:
        print(0)