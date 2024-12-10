N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 기준으로 정렬 (끝나는 시간이 같으면 시작 시간으로 정렬)
I.sort(key=lambda x: (x[1], x[0]))

ans = 0
end_time = 0

for start_time, finish_time in I:
    if start_time >= end_time:  # 현재 회의 시작 시간이 이전 회의 종료 시간 이후라면
        ans += 1
        end_time = finish_time  # 종료 시간을 갱신

print(ans)
