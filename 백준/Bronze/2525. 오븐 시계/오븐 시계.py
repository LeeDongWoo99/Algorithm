A, B = map(int, input().split())
C = int(input())

B += C

if B >= 60:
    S = B // 60
    B = B % 60
    A += S
    if A >= 24:
        A -= 24

print(f"{A} {B}")
    

