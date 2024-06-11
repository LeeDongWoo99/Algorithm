import sys
input = sys.stdin.readline

# 수행해야 하는 연산의 수
M = int(input().strip())
S = set()

for _ in range(M):
    order = input().strip().split()
    # 리스트에 명령어 부분만 추출
    ord = order[0]

    if len(order) > 1:
        x = int(order[1])

    if ord == "add":
        S.add(x)

    elif ord == "remove":
        S.discard(x)  # discard를 사용하면 try-except가 필요 없습니다.

    elif ord == "check":
        if x in S:
            print(1)
        else:
            print(0)

    elif ord == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif ord == "all":
        S = set(range(1, 21))

    elif ord == "empty":
        S.clear()
