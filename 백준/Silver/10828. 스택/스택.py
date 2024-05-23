import sys

# 명령의 수
cnt = int(sys.stdin.readline())
# stack 선언
lst = []
for _ in range(cnt):
    ord = sys.stdin.readline().split()
    if ord[0] == "push":
        lst.append(int(ord[1]))
    elif ord[0] == "size":
        print(len(lst))
    elif ord[0] == "pop":
        if not lst:
            print(-1)
        else:
            print(lst.pop())
    elif ord[0] == "empty":
        if not lst:
            print(1)
        else:
            print(0)
    elif ord[0] == "top":
        if not lst:
            print(-1)
        else:
            print(lst[-1])
