def solution(n, arr1, arr2):
    ans = []
    
    for i in range(n):
        # 각 숫자를 이진수로 변환하고 n 길이만큼 앞에 0을 추가
        bin1 = format(arr1[i], 'b').zfill(n)
        bin2 = format(arr2[i], 'b').zfill(n)
        
        # 두 이진수를 OR 연산하여 결합
        combined = int(bin1, 2) | int(bin2, 2)
        
        # 결합한 결과를 이진수 문자열로 변환하고 앞에 0을 추가
        combined_bin = format(combined, 'b').zfill(n)
        
        # 이진수 문자열을 "#"과 " "로 변환
        row = combined_bin.replace("0", " ").replace("1", "#")
        
        ans.append(row)
    
    return ans