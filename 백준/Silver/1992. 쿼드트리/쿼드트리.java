import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static StringBuilder sb = new StringBuilder();

    // 현재 영역이 모두 같은 숫자인지 확인하는 함수
    public static boolean isSingleColor(int x, int y, int size, int[][] video) {
        int color = video[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (video[i][j] != color) {
                    return false;
                }
            }
        }
        return true;
    }

    // 쿼드트리 압축을 수행하는 함수
    public static void compress(int x, int y, int size, int[][] video) {
        if (isSingleColor(x, y, size, video)) {
            // 현재 영역이 같은 숫자라면 해당 숫자를 추가
            sb.append(video[x][y]);
        } else {
            // 영역을 4개로 나누어 재귀 호출
            sb.append("("); // 시작 괄호 추가
            int half = size / 2;
            compress(x, y, half, video); // 왼쪽 위
            compress(x, y + half, half, video); // 오른쪽 위
            compress(x + half, y, half, video); // 왼쪽 아래
            compress(x + half, y + half, half, video); // 오른쪽 아래
            sb.append(")"); // 끝 괄호 추가
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 처리
        int n = Integer.parseInt(br.readLine());
        int[][] video = new int[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                video[i][j] = line.charAt(j) - '0'; // 문자를 숫자로 변환
            }
        }

        // 쿼드트리 압축 시작
        compress(0, 0, n, video);

        // 결과 출력
        System.out.println(sb.toString());
    }
}