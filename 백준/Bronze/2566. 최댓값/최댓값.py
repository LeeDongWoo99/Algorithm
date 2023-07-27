ls = [list(map(int,input().split())) for _ in range(9)]

max_num = ls[0][0]
max_row = 0
max_column = 0

for row in range(9):
    for column in range(9):
        if max_num <= ls[row][column]:
            max_row = row + 1
            max_column = column + 1
            max_num = ls[row][column]
print(max_num)
print(max_row,max_column)
