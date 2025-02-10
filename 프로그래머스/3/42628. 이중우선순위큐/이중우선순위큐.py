import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for cmd in operations:
        lst = cmd.split()
        if lst[0] == "I":
            num = int(lst[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            
        elif lst[0] == "D" and min_heap:
            if lst[1] == "1":
                max_num = -heapq.heappop(max_heap)
                min_heap.remove(max_num)
            elif lst[1] == "-1":
                min_num = heapq.heappop(min_heap)
                max_heap.remove(-min_num)
                
        if not min_heap:
            min_heap.clear()
            max_heap.clear()
            
    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]  
    else:
        return [0, 0]