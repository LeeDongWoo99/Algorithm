def solution(n, arr1, arr2):
    ans = []
    
    for i in range(n):
        chk = arr1[i] | arr2[i]
        lst = bin(chk)[2:].zfill(n)  # 이진수로 변환하고 앞에 0을 채워 길이를 맞춤
        lst = lst.replace("0", " ").replace("1", "#")
        ans.append(lst)
    return ans
    
