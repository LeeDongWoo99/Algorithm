import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville) # 최소힙으로 변환
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        count += 1
        
    return count