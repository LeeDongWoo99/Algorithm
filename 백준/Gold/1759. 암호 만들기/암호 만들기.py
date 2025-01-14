import sys
input = sys.stdin.readline

def check():
    vowels_count = 0
    consonants_count = 0
    for char in ans:
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    return vowels_count >= 1 and consonants_count >= 2


def dfs(depth, start):
    if depth == L:
        if check():
            print("".join(ans))
        return

    for i in range(start, C):
        ans.append(apb[i])
        dfs(depth + 1, i + 1)
        ans.pop()


L, C = map(int, input().split())
apb = list(input().split())
apb.sort()
ans = []
vowels = {'a', 'e', 'i', 'o', 'u'}

dfs(0, 0)