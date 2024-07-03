import heapq

def solution(jobs):
    ans = 0
    now = 0 # 현재 시점
    count = 0 # 완료한 작업 수
    start = -1 # 마지막 작업이 끝난 시간
    heap = []
    
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
                
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            ans += now - current[1]
            count += 1
        else:
            now +=1
    return int(ans // len(jobs))