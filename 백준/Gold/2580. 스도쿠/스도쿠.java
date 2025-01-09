import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static final int SIZE = 9;
    public static final int BOX_SIZE = 3;
    public static int[][] arr = new int[SIZE][SIZE];
    public static List<int[]> blank = new ArrayList<>();

    public static boolean possibility(int row, int col, int value) {

        // 행 열 체크
        for (int i = 0; i < SIZE; i++) {
            if (arr[row][i] == value || arr[i][col] == value) {
                return false;
            }
        }

        // 3*3 칸에 중복되는 원소가 있는지 검사
        int set_row = (row / BOX_SIZE) * BOX_SIZE; // value가 속한 3x3의 행의 첫 위치
        int set_col = (col / BOX_SIZE) * BOX_SIZE; // value가 속한 3x3의 열의 첫 위치

        for (int i = set_row; i < set_row + BOX_SIZE; i++) {
            for (int j = set_col; j < set_col + BOX_SIZE; j++) {
                if (arr[i][j] == value) {
                    return false;
                }
            }
        }

        return true; // 중복되는 것이 없을 경우 true 반환
    }

    public static void sudoku(int n) {

        // 해당 행이 다 채워졌을 경우 다음 행의 첫 번째 열부터 시작
        if (n == blank.size()) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < SIZE; i++) {
                for (int j = 0; j < SIZE; j++) {
                    sb.append(arr[i][j]).append(' ');
                }
                sb.append('\n');
            }
            System.out.println(sb);
            // 출력 뒤 시스템을 종료한다.
            System.exit(0);
        }

        // 현재 빈칸의 좌표
        int[] coord = blank.get(n);
        int y = coord[0];
        int x = coord[1];


        // 만약 해당 위치의 값이 0 이라면 1부터 9까지 중 가능한 수 탐색
        for (int checkNum = 1; checkNum <= 9; checkNum++) {
            if (possibility(y, x, checkNum)) {
                arr[y][x] = checkNum;
                sudoku(n + 1);
                arr[y][x] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < SIZE; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < SIZE; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 0) {
                    blank.add(new int[]{i, j});
                }
            }
        }

        sudoku(0);

    }
}