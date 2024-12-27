import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static int[][] board;
    public static int[] result = new int[2];

    public static boolean isCheckCount(int x, int y, int size) {
        int color = board[x][y];
        for(int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (color != board[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    public static void colorCount(int x, int y, int size) {
        if (isCheckCount(x, y, size)) {
            result[board[x][y]] +=1;
        } else {
            int half = size / 2;
            colorCount(x, y, half);
            colorCount(x, y+half, half);
            colorCount(x + half, y, half);
            colorCount(x + half, y + half, half);
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        for (int i = 0; i < N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(row[j]);
            }
        }
        colorCount(0, 0, N);

        System.out.println(result[0]);
        System.out.println(result[1]);
    }
}