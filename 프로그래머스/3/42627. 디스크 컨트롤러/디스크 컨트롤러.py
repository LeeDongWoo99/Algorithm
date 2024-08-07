import heapq

def solution(jobs):
    start = -1 # 마지막 작업이 시작한 시점
    now = 0 # 현재 시점
    ans = 0 # 총 작업에 걸린 시간
    heap = []
    count = 0
    
    while count < len(jobs):
        for job in jobs:
            if start < job[0] <= now: 
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            ans += now - current[1]
            count +=1
        else:
            now +=1
            
    return int(ans // len(jobs))