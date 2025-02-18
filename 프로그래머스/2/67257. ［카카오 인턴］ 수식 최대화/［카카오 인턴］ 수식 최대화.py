from itertools import permutations

def operation(num1, num2, op):  
    """ 연산자에 따라 수식을 계산하는 함수 """
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(exp, op_order):  
    """ 연산자 우선순위에 맞게 계산하는 함수 """
    array = exp[:]  # 원본 리스트 복사
    for o in op_order:
        stack = []
        while array:
            tmp = array.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))

def parse_expression(expression):
    """ 주어진 수식을 숫자와 연산자로 분리하는 함수 """
    tokens = []
    tmp = ""
    for char in expression:
        if char.isdigit():
            tmp += char
        else:
            tokens.append(tmp)
            tokens.append(char)
            tmp = ""
    tokens.append(tmp)
    return tokens

def solution(expression):
    op_orders = list(permutations(['+', '-', '*'], 3))  # 연산자 우선순위 조합
    tokens = parse_expression(expression)  # 숫자와 연산자 분리 (한 번만 수행)
    return max(calculate(tokens, op_order) for op_order in op_orders)