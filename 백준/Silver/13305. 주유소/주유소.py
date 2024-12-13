N = int(input()) # 도시의 개수
dis = list(map(int, input().split())) # 각 도시까지의 거리
oil = list(map(int, input().split())) # 각 주요소의 가격
min_oil = oil[0]

ans = dis[0] * oil[0]

for cur in range(1, N-1):
    if min_oil > oil[cur]:
        min_oil = oil[cur]
    ans += min_oil * dis[cur]

print(ans)