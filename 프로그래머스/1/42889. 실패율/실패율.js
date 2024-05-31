function solution(N, stages) {
    // 총 플레이어 수
    let player = stages.length;
    // 실패율을 저장할 객체
    let failRate = {};
    
    for (let stage = 1; stage <= N; stage++) {
        let count = stages.filter(s => s === stage).length;  // 해당 스테이지에 도달한 플레이어 수
        if (player !== 0) {
            failRate[stage] = count / player;  // 실패율 계산
            player -= count;  // 남은 플레이어 수 업데이트
        } else {
            failRate[stage] = 0;  // 남은 플레이어가 없으면 실패율은 0
        }
    }

    // 실패율 기준으로 내림차순 정렬
    let sortedStages = Object.keys(failRate).sort((a, b) => failRate[b] - failRate[a]);
    
    // 정렬된 스테이지 번호를 정수형으로 변환
    return sortedStages.map(Number);
}
