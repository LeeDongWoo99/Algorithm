import heapq

def solution(jobs):
    answer = 0
    now = 0  # 현재시간
    i = 0  # 처리된 작업 개수
    start = -1  # 마지막 완료 시간
    heap = []
    
    while i < len(jobs):
        # 현재 시간에 시작할 수 있는 작업들을 힙에 추가
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        
        # 힙에 작업이 있다면, 가장 소요 시간이 짧은 작업을 꺼내서 처리
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += now - current[1]  # 요청으로부터 처리 시간
            i += 1
        else:
            # 현재 시간에 처리할 작업이 없다면 시간을 증가시킴
            now += 1
    
    return answer // len(jobs)
