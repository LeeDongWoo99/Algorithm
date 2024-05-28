function solution(s) {
    // 각 숫자에 대한 단어
    let num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    var lst = s;

    for (let i = 0; i < num.length; i++) {
        let arr = lst.split(num[i]);
        lst = arr.join(i);
    }
    return Number(lst);
}