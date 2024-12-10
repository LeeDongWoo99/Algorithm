N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]

I.sort(key=lambda x: (x[1], x[0]))

ans = 0
end_time = 0

for start_time, finish_time in I:
    if start_time >= end_time:
        ans += 1
        end_time = finish_time
print(ans)
