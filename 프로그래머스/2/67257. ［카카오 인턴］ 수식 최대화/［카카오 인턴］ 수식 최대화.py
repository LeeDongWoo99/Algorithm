import re
from itertools import permutations

def solution(expression):
    tokens = re.split(r'(\D)', expression)
    numbers = list(map(int, tokens[::2]))
    ops = tokens[1::2]
    
    max_ans = 0
    
    for op_order in permutations(["+", "-", "*"]):
        nums = numbers[:]
        ops_copy = ops[:]
        
        for op in op_order:
            while op in ops_copy:
                idx = ops_copy.index(op)
                
                if op == "+":
                    result = nums[idx] + nums[idx + 1]
                elif op == "-":
                    result = nums[idx] - nums[idx + 1]
                elif op == "*":
                    result = nums[idx] * nums[idx + 1]
                
                nums[idx] =  result
                del nums[idx + 1]
                del ops_copy[idx]
                
        max_ans = max(max_ans, abs(nums[0]))
    return max_ans
