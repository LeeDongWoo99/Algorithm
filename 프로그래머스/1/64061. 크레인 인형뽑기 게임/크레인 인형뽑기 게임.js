function solution(board, moves) {
    let basket = [];
    var result = 0;
    for(move of moves) {
        for(row of board) {
            if (row[move-1] != 0) {
                let doll = row[move-1];
                row[move-1] = 0
                if(basket.length != 0 && basket[basket.length - 1] === doll) { 
                    result += 2
                    basket.pop()
                }
                else {
                    basket.push(doll)
                }
                break
            }
        }
    }

    return result;
}