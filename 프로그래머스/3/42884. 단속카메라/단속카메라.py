def solution(routes):
    routes.sort(key = lambda x: x[1])
    camara = routes[0][1]
    answer = 1
    
    for i in range(1, len(routes)):
        if camara >= routes[i][0]:
            continue
        else:
            camara = routes[i][1]
            answer += 1
            
    return answer