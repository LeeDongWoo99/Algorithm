import heapq

def solution(scoville, K):
    heapq.heapify(scoville) 
    ans = 0
    
    while len(scoville) >= 2:
        min_ = heapq.heappop(scoville)
        if min_ >= K:
            return ans
        else:
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_ + 2 * min_2)
            ans += 1
    
    if scoville and scoville[0] >= K:
        return ans
    
    return -1
