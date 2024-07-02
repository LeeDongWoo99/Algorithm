import heapq

def solution(jobs):
    now = 0
    ans = 0
    count = 0
    total_jobs = len(jobs)
    heap = []

    while count < total_jobs:
        to_remove = []
        for job in jobs:
            if job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
                to_remove.append(job)

        # 제거할 작업들을 한 번에 제거
        for job in to_remove:
            jobs.remove(job)
        
        if heap:
            current_job = heapq.heappop(heap)
            now += current_job[0]
            ans += now - current_job[1]
            count += 1
        else:
            now += 1

    return int(ans // total_jobs)