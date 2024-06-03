function solution(board, moves) {
    var result = 0;
    let basket = [];
    for (let i = 0; i < moves.length; i++) {
        for (let j = 0; j < board.length; j++) {
            // 현재 행에서 크레인 위치에 인형이 있는 경우
            if (board[j][moves[i] - 1] !== 0) {
                let doll = board[j][moves[i] - 1];
                board[j][moves[i] - 1] = 0;
                if (basket.length !== 0 && basket[basket.length - 1] === doll) {
                    result += 2;
                    basket.pop();
                } else {
                    basket.push(doll);
                }
                break;
            }
        }
    }
    return result;
}
