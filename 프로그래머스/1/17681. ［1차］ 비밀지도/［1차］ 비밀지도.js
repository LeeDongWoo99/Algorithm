function solution(n, arr1, arr2) {
    let ans = [];
    
    for (let i = 0; i < n; i++) {
        // 각 숫자를 이진수로 변환하고 n 길이만큼 앞에 0을 추가
        let bin1 = arr1[i].toString(2).padStart(n, '0');
        let bin2 = arr2[i].toString(2).padStart(n, '0');
        
        // 두 이진수를 OR 연산하여 결합
        let combined = "";
        for (let j = 0; j < n; j++) {
            if (bin1[j] === '1' || bin2[j] === '1') {
                combined += '#';
            } else {
                combined += ' ';
            }
        }
        
        ans.push(combined);
    }
    
    return ans;
}
