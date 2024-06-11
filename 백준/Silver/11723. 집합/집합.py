import sys
input = sys.stdin.readline

# 수행해야 하는 연산의 수
M = int(input())
S = []

for _ in range(M):
    order = input().split()
    ord = order[0]

    if ord == "add":
        x = int(order[1])
        if x not in S:
            S.append(x)

    elif ord == "remove":
        x = int(order[1])
        if x in S:
            S.remove(x)

    elif ord == "check":
        x = int(order[1])
        if x in S:
            print(1)
        else:
            print(0)

    elif ord == "toggle":
        x = int(order[1])
        if x in S:
            S.remove(x)
        else:
            S.append(x)

    elif ord == "all":
        S = [i for i in range(1, 21)]

    elif ord == "empty":
        S = []