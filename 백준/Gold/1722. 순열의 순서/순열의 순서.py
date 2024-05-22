import math

def find_one(n, k):
    # 수열을 나타내는 결과값이 하나가 남았을 때, numbers 리스트에 있는 마지막 요소 추가
    # 즉, 남은 숫자가 하나밖에 없으니깐 결과값에 추가
    if len(ans) == N - 1:
        ans.append(numbers[-1])
        return
    # 맨 앞이 numbers 안에 있는 요소 중 하나일 때 나올 수 있는 경우의 수
    case = math.factorial(n) // n
    # 어느 numbers 안에 있는 숫자가 k번째 수열에 가까운지 계산
    sequence = math.ceil(k / case)
    # sequence 값을 numbers 안에 있는 값을 제거하기 위해  sequence-1 수행, 리스트에 인덱스 번호는 0부터 시작이기 때문에 -1을 해줘야 한다.
    ans.append(numbers.pop(sequence-1))
    find_one(n-1, k-(case * (sequence-1)))
    
def find_k():
    n = N
    for num in k:
        case = math.factorial(n) // n 
        idx = numbers.index(num)
        if len(numbers) == 2:
            idx += 1
            ans.append(case*idx)
            return
        numbers.pop(idx)
        ans.append(case*idx)
        n -= 1
        
N = int(input())
lst = list(map(int, input().split()))
ord = lst.pop(0)

# 소문제 1
if ord == 1:
    k = lst[0]
    numbers = [x for x in range(1, N+1)]
    ans = []
    find_one(N, k)
    print(" ".join(list(map(str, ans))))
    
    # 소문제 2
else:
    k = lst
    numbers = [x for x in range(1, N+1)]
    ans = []
    find_k()
    print(sum(ans))