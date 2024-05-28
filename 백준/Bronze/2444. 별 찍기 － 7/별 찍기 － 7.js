const fs = require('fs');

// 입력을 파일로부터 읽어오는 방식
const input = fs.readFileSync('/dev/stdin').toString().trim();

// 입력을 숫자로 변환
const n = parseInt(input, 10);

// 첫 번째 피라미드 부분
for (let i = 1; i <= n; i++) {
    console.log(" ".repeat(n - i) + "*".repeat(i * 2 - 1));
}

// 두 번째 피라미드 부분
for (let j = 1; j < n; j++) {
    console.log(" ".repeat(j) + "*".repeat(n * 2 - j * 2 - 1));
}
