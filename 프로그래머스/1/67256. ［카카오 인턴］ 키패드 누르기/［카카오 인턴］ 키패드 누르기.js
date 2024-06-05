function solution(numbers, hand) {
    var result = "";
    let left = [3, 0]; // '*' 위치
    let right = [3, 2]; // '#' 위치

    hand = hand === "left" ? "L" : "R";

    let keypad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        0: [3, 1]
    };

    for (let num of numbers) {
        if ([1, 4, 7].includes(num)) {
            result += "L";
            left = keypad[num];
        } else if ([3, 6, 9].includes(num)) {
            result += "R";
            right = keypad[num];
        } else {
            let target = keypad[num];
            let left_dist = Math.abs(left[0] - target[0]) + Math.abs(left[1] - target[1]);
            let right_dist = Math.abs(right[0] - target[0]) + Math.abs(right[1] - target[1]);

            if (left_dist < right_dist) {
                result += "L";
                left = target;
            } else if (right_dist < left_dist) {
                result += "R";
                right = target;
            } else {
                if (hand === "L") {
                    result += "L";
                    left = target;
                } else {
                    result += "R";
                    right = target;
                }
            }
        }
    }

    return result;
}
