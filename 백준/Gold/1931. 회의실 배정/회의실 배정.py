N = int(input())
I = [list(map(int, input().split())) for _ in range(N)] # 회의 시작 시관과 종료 시간을 저장할 2차원 배열 생성

I.sort(key=lambda x: (x[1], x[0]))


ans = 0
end_time = 0

for start_time, finish_time in I:
    if start_time >= end_time:
        ans +=1
        end_time = finish_time
print(ans)
