from itertools import permutations

def is_prime(num):
    if num == 2:
        return True
    if num < 2:
        return False
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
            break
    return True


def solution(numbers):
    num = [ch for ch in numbers]
    per = []
    ans = 0
    for i in range(1, len(numbers) + 1):
        per += list(permutations(num, i))
        lst = [int("".join(n)) for n in per]
    
    for ls in lst:
        if is_prime(ls):
            ans += 1

    return ans