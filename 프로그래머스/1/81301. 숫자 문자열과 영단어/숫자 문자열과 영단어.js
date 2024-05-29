function solution(s) {
    let num = ["zero", "one", "two", "three", "four", "five", "six", "seven","eight","nine"] 
    var lst = s
    
    for (let i = 0; i <num.length; i++) {
        let arr = lst.split(num[i]);
        lst = arr.join(i)
    }
    return Number(lst);
}