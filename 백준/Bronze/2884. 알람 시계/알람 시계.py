#알람을 설정할 시와 분을 입력받는다.
H, M = map(int, input().split())
M -= 45
if M < 0:
        M = 60 - abs(M)
        H -= 1
        if H < 0:
            H = 24 - abs(H)

print(f"{H} {M}")