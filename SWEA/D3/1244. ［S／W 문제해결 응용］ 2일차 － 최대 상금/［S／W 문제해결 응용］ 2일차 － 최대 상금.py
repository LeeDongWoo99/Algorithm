def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int("".join(lst)))
        return

    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]
            chk = int("".join(lst)) + n
            if chk not in v:
                v.append(chk)
                dfs(n + 1)
            lst[i], lst[j] = lst[j], lst[i]

t = int(input()) # 테스트 개수
for tc in range(1 , t + 1):
    st, c = input().split()
    ans = 0
    lst = []
    N = int(c)
    for i in st:
        lst.append(i)
    L = len(lst)
    v = [] # 방문 배열
    dfs(0)

    print(f'#{tc} {ans}')