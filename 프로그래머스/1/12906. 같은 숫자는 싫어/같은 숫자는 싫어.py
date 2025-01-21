def solution(arr):
    ans = []
    ans.append(arr[0])
    for num in range(1, len(arr)):
        if ans[-1] != arr[num]:
            ans.append(arr[num])
        else:
            continue
    return ans
            