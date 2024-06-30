def solution(brown, yellow):
    total = brown + yellow
    ans = []
    for i in range(1, int(total ** 0.5) +1):
        if total % i == 0:
            width = total // i
            if (width -2) * (i - 2) == yellow:
                return [width, i]