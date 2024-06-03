function solution(dartResult) {
    let score = [];
    let i = 0;

    while (i < dartResult.length) {
        if (isDigit(dartResult[i])) {
            let num;
            if (i + 1 < dartResult.length && isDigit(dartResult[i + 1])) {
                num = parseInt(dartResult[i] + dartResult[i + 1]);
                i += 1;
            } else {
                num = parseInt(dartResult[i]);
            }

            if (dartResult[i + 1] === 'S') {
                num **= 1;
            } else if (dartResult[i + 1] === 'D') {
                num **= 2;
            } else if (dartResult[i + 1] === 'T') {
                num **= 3;
            }
            score.push(num);

            i += 1;
        } else if (dartResult[i] === '*') {
            if (score.length > 0) {
                score[score.length - 1] *= 2;
            }
            if (score.length > 1) {
                score[score.length - 2] *= 2;
            }
        } else if (dartResult[i] === '#') {
            if (score.length > 0) {
                score[score.length - 1] *= -1;
            }
        }
        i += 1;
    }

    let result = score.reduce((acc, curr) => acc + curr, 0);
    return result;
}

function isDigit(char) {
    return !isNaN(char) && char !== ' ';
}