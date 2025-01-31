import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first_food = heapq.heappop(scoville)
        second_food = heapq.heappop(scoville)
        new_food = first_food + (second_food * 2)
        heapq.heappush(scoville, new_food)
        count += 1
        
    return count