def dfs(n):
    # 교환 횟수가 최대 교환 횟수일 때
    global ans
    if n == N:
        ans = max(ans, int(''.join(map(str, lst))))
        return

    for i in range(L-1):
        for j in range(i+1, L):
            lst[i], lst[j] = lst[j],lst[i]

            chk = int(''.join(map(str, lst))) *10 + n
            if chk not in v:
                dfs(n+1)
                v.append(chk)
            lst[i], lst[j] = lst[j], lst[i]



tc = int(input())

for tc in range(1, tc+1):
    st, t = input().split()
    # 최대 교환 횟수
    N = int(t)
    lst = []
    # 문자열을 리스트로 변환
    for ch in st:
        lst.append(ch)
    # 방문 리스트
    v = []
    # 최대값
    ans = 0
    # 교환 횟수
    L = len(lst)
    dfs(0)
    print(f"#{tc} {ans}")