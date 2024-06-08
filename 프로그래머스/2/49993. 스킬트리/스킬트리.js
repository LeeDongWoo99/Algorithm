function solution(skill, skill_trees) {
    var result = 0;

    for (let skill_tree of skill_trees) {
        var skill_order = [];

        for (let sk of skill_tree) {
            if (skill.includes(sk)) {
                skill_order.push(sk);
            }
        }

        let is_valid = true;  // 이 부분은 if 블록 내부로 이동
        for (let i = 0; i < skill_order.length; i++) {
            if (skill_order[i] != skill[i]) {
                is_valid = false; // 조건에 맞지 않는 경우 플래그를 변경하고 루프 종료
                break;
            }
        }

        if (is_valid) {
            result += 1;  // 유효한 스킬 순서인 경우 결과값 증가
        }
    }

    return result;
}
