def pow(A, B):
    if B == 1:
        return A % C

    temp = pow(A, B // 2)

    if B % 2 == 1:
        return (temp * temp % C) * A % C
    return temp * temp % C

A, B, C = map(int, input().split())

print(pow(A, B))