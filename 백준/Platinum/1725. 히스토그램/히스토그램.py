import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
    
stack = []
max_rst = 0

for i in range(N):
    idx = i
    
    while stack and stack[-1][1] > lst[i]:
        idx, height = stack.pop()
        rst = (i - idx) * height
        max_rst = max(max_rst, rst)
    stack.append([idx, lst[i]])
    
while stack:
    idx, height = stack.pop()
    rst = (N - idx) * height
    max_rst = max(max_rst, rst)
    
print(max_rst)