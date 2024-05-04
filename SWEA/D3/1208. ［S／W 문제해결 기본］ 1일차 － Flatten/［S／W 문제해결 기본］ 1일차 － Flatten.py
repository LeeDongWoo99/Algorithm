T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 덤프를 입력받는다.
    dump = int(input())
    # 1000개의 박스 높이를 입력받는다.
    #for i in range(10):
    lst = list(map(int, input().split()))
    for _ in range(dump):
        lst.sort(reverse=True)
        lst[0] -=1
        lst[-1] +=1

    
    print(f'#{test_case} {max(lst) - min(lst)}')