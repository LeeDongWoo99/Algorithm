function solution(input) {
    let s = input;  // 여기서 s를 명시적으로 선언합니다.
    const num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    };

    for (let key in num) {
        s = s.split(key).join(num[key]);
    }

    return parseInt(s, 10);
}