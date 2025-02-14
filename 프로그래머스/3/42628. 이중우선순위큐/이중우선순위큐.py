import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    
    for command in operations:
        cmd = command.split()
        if cmd[0] == "I": # 명령어 첫 부분이 입력이라면
            num = int(cmd[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif cmd[0] == "D":
            if cmd[1] == "-1" and min_heap: # 명령어 뒷 부분이 -1이라면, 최소값 삭제
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
            if cmd[1] == "1" and min_heap: # 명령어 뒷 부분이 1이라면
                max_val = -heapq.heappop(max_heap)
                min_heap.remove(max_val)
            
    if max_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0,0]
