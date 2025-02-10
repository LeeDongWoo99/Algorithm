def solution(prices):
    ans = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        ans[j] = len(prices) -1 - j
    
    return ans