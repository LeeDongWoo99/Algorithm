def solution(sizes):
    # 각 명함의 가로와 세로를 정렬
    sorted_sizes = [sorted(size, reverse=True) for size in sizes]
    
    # 가로의 최대값과 세로의 최대값 계산
    max_width = max(size[0] for size in sorted_sizes)  # 가로 중 가장 큰 값
    max_height = max(size[1] for size in sorted_sizes)  # 세로 중 가장 큰 값
    
    # 최소 지갑 크기 계산
    return max_width * max_height