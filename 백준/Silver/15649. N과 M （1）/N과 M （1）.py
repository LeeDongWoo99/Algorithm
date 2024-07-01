from itertools import permutations

N, M = map(int, input().split())

lst = [str(i) for i in range(1, N + 1)]
ans = permutations(lst, M)

for i in ans:
    print(' '.join(i))