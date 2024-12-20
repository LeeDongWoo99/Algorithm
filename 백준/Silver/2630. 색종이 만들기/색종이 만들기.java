import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    // 현재 영역이 모두 같은 색인지 확인하는 함수
    public static boolean isSingleColor(int x, int y, int size, int[][] paper) {
        int color = paper[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (paper[i][j] != color) {
                    return false;
                }
            }
        }
        return true;
    }

    // 분할 정복을 통해 색상 개수를 세는 함수
    public static void countColors(int x, int y, int size, int[][] paper, int[] result) {
        if (isSingleColor(x, y, size, paper)) {
            // 현재 영역이 같은 색이라면 카운트 증가
            result[paper[x][y]]++;
        } else {
            // 영역을 4개로 나누어 재귀 호출
            int half = size / 2;
            countColors(x, y, half, paper, result); // 왼쪽 위
            countColors(x, y + half, half, paper, result); // 오른쪽 위
            countColors(x + half, y, half, paper, result); // 왼쪽 아래
            countColors(x + half, y + half, half, paper, result); // 오른쪽 아래
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 처리
        int n = Integer.parseInt(br.readLine()); // 첫 번째 입력, 종이의 크기
        int[][] paper = new int[n][n];

        // 종이의 색 정보를 입력받아 paper 배열에 저장
        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split(" ");  // 공백을 기준으로 입력을 나눔
            for (int j = 0; j < n; j++) {
                paper[i][j] = Integer.parseInt(row[j]);  // 각 값을 정수로 변환하여 저장
            }
        }

        // 결과 저장 (하얀색, 파란색 순서)
        int[] result = new int[2];

        // 분할 정복 시작
        countColors(0, 0, n, paper, result);

        // 결과 출력
        System.out.println(result[0]); // 하얀색 개수
        System.out.println(result[1]); // 파란색 개수
    }
}