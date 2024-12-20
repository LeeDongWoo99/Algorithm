import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static boolean isSingleColor(int x, int y, int size, int[][] board) {
        int color = board[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (board[i][j] != color) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void countColors(int x, int y, int size, int[][] board) {
        if (isSingleColor(x, y, size, board)) {
            int color = board[x][y];
            if (color == -1) {
                result[0]++; // -1 (GRAY)
            } else if (color == 0) {
                result[1]++; // 0 (WHITE)
            } else {
                result[2]++; // 1 (BLACK)
            }
        } else {
            int newSize = size / 3;

            // 9개의 구역으로 나눔
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    countColors(x + i * newSize, y + j * newSize, newSize, board);
                }
            }
        }
    }

    public static int[] result = new int[3]; // -1, 0, 1의 개수를 저장

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N 크기 입력받기
        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];

        // 2차원 배열 입력
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 분할 정복 수행
        countColors(0, 0, n, board);

        // 결과 출력
        System.out.println(result[0]); // -1 (GRAY) 개수
        System.out.println(result[1]); // 0 (WHITE) 개수
        System.out.println(result[2]); // 1 (BLACK) 개수
    }
}