N = int(input())

result = 0

for num in range(1, N+1):
    lst = list(map(int, str(num)))
    result = sum(lst) + num
    if result == N:
        print(num)
        break
    if N == num: # 입력값과 num이 같다는 것은, 반복문이 끝날때 까지 생성자 값이 안나왔다는 뜻이다.
        print(0)