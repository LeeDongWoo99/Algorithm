import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 입력받기
        int N = sc.nextInt();
        int M = sc.nextInt();
        sc.nextLine(); // 개행 처리
        String[] board = new String[N];
        for (int i = 0; i < N; i++) {
            board[i] = sc.nextLine();
        }

        // 체스판 패턴 정의
        String[] chessW = {
                "WBWBWBWB",
                "BWBWBWBW",
                "WBWBWBWB",
                "BWBWBWBW",
                "WBWBWBWB",
                "BWBWBWBW",
                "WBWBWBWB",
                "BWBWBWBW"
        };

        String[] chessB = {
                "BWBWBWBW",
                "WBWBWBWB",
                "BWBWBWBW",
                "WBWBWBWB",
                "BWBWBWBW",
                "WBWBWBWB",
                "BWBWBWBW",
                "WBWBWBWB"
        };

        // 최소값 초기화
        int minPaint = Integer.MAX_VALUE;

        // 모든 8x8 체스판 탐색
        for (int i = 0; i <= N - 8; i++) { // 가능한 행 시작점
            for (int j = 0; j <= M - 8; j++) { // 가능한 열 시작점
                int paintW = 0; // W로 시작하는 체스판과의 차이
                int paintB = 0; // B로 시작하는 체스판과의 차이

                // 8x8 체스판 체크
                for (int x = 0; x < 8; x++) {
                    for (int y = 0; y < 8; y++) {
                        if (board[i + x].charAt(j + y) != chessW[x].charAt(y)) {
                            paintW++;
                        }
                        if (board[i + x].charAt(j + y) != chessB[x].charAt(y)) {
                            paintB++;
                        }
                    }
                }
                // 최소값 갱신
                minPaint = Math.min(minPaint, Math.min(paintW, paintB));
            }
        }

        // 결과 출력
        System.out.println(minPaint);
    }
}