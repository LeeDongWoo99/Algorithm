from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)  
queue = deque([(arr, 0)])  
visited = set()  

while queue:
    current, count = queue.popleft()

    if current == sorted_arr:
        print(count)
        exit()  

    current_tuple = tuple(current)
    if current_tuple in visited:
        continue
    visited.add(current_tuple)

    for i in range(n - k + 1):
        new_list = current[:i] + current[i:i + k][::-1] + current[i + k:]
        queue.append((new_list, count + 1))

print(-1)
