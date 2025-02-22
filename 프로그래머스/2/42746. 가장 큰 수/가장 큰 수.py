def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x * 3, reverse = True)
    
    numbers = "".join(numbers)
    
    return "0" if numbers[0] == "0" else numbers