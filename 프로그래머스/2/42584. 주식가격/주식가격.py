def solution(prices):
    result = []
    for idx in range(len(prices)):
        ans = 0
        for i in range(idx, len(prices) -1):
            ans += 1
            if prices[idx] > prices[i + 1]:
                break
        result.append(ans)
    return result