import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for command in operations:
        cmd = command.split()
        
        if cmd[0] == "I":
            num = int(cmd[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            
        elif cmd[0] == "D" and min_heap:
            if cmd[1] == "-1":
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
            elif cmd[1] == "1":
                max_val = -heapq.heappop(max_heap)
                min_heap.remove(max_val)
                
    if max_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
