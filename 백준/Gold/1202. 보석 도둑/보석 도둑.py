import sys
import heapq

input = sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())  # 보석 개수(n), 가방 개수(k)
jewels = []  # (무게, 가치)
bags = []  # 가방 무게 리스트

# 보석 정보 저장
for _ in range(n):
    m, v = map(int, input().split())  # 무게, 가치
    jewels.append((m, v))

# 가방 정보 저장
for _ in range(k):
    bags.append(int(input().strip()))

# 1. 보석을 무게 기준으로 오름차순 정렬
jewels.sort()
# 2. 가방을 무게 기준으로 오름차순 정렬
bags.sort()

# 우선순위 큐 (최대 힙) 사용
max_heap = []
total_value = 0
jewel_idx = 0

# 3. 가방을 하나씩 탐색하면서, 담을 수 있는 보석들을 최대 힙에 추가
for bag in bags:
    # 현재 가방이 담을 수 있는 모든 보석을 최대 힙에 추가
    while jewel_idx < n and jewels[jewel_idx][0] <= bag:
        heapq.heappush(max_heap, -jewels[jewel_idx][1])  # 최대 힙을 위해 음수로 저장
        jewel_idx += 1

    # 4. 가장 가치가 높은 보석을 선택
    if max_heap:
        total_value += -heapq.heappop(max_heap)  # 최대 힙에서 가장 가치가 높은 보석 선택

# 결과 출력
print(total_value)
