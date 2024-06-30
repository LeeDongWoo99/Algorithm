def solution(brown, yellow):
    total = brown + yellow  # 전체 타일 수
    
    # 전체 타일 수의 약수 구하기
    for height in range(1, int(total ** 0.5) + 1):
        if total % height == 0:
            width = total // height
            # 갈색 테두리 타일 고려한 노란색 타일 크기 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]