function solution(n, arr1, arr2) {
    let ans = [];

    for (let i = 0; i < n; i++) {
        let chk = arr1[i] | arr2[i];
        let lst = chk.toString(2).padStart(n, '0'); // 2진수로 변환하고 앞에 0을 채워 길이를 맞춤
        lst = lst.replace(/0/g, ' ').replace(/1/g, '#');
        ans.push(lst);
    }
    
    return ans;
}