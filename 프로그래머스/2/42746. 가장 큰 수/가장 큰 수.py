def solution(numbers):
    nums = list(map(str, numbers)) # 각 요소들을 문자열로 변환
    nums.sort(key = lambda x: x * 3, reverse = True)
    
    result = "".join(nums)
    
    return "0" if result[0] == "0" else result
