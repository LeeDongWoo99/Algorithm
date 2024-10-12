import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  // 표준 입력으로 변경
        int T = 10;  // 테스트 케이스 개수

        for (int tc = 1; tc <= T; ++tc) {
            int t = sc.nextInt();  // 테스트 케이스 번호
            int N = 100;  // 배열 크기
            int[][] arr = new int[N][N];  // 배열 생성

            // 배열 입력 받기
            for (int i = 0; i < N; ++i) {
                for (int j = 0; j < N; ++j) {
                    arr[i][j] = sc.nextInt();
                }
            }

            int ans = 0;  // 최대값 저장
            int s3 = 0;   // 좌상-우하 대각선 합
            int s4 = 0;   // 우상-좌하 대각선 합

            // 행과 열의 합, 대각선 합 계산
            for (int i = 0; i < N; ++i) {
                int s1 = 0;  // 행의 합
                int s2 = 0;  // 열의 합

                for (int j = 0; j < N; ++j) {
                    s1 += arr[i][j];  // 행의 합
                    s2 += arr[j][i];  // 열의 합
                }

                // 최대값 갱신
                ans = Math.max(ans, Math.max(s1, s2));

                // 대각선 합 계산
                s3 += arr[i][i];  // 좌상-우하 대각선
                s4 += arr[i][N - i - 1];  // 우상-좌하 대각선
            }

            // 대각선 합과 행, 열 최대값 비교 후 갱신
            ans = Math.max(ans, Math.max(s3, s4));

            // 결과 출력
            System.out.println("#" + t + " " + ans);
        }

        sc.close();
    }
}
