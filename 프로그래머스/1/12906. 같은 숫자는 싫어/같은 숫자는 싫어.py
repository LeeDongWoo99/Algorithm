def solution(arr):
    ans = []
    ans.append(arr[0])
    for i in range(1, len(arr)):
        if ans[-1] == arr[i]:
            continue
        ans.append(arr[i])
    return ans