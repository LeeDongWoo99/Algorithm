import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();  // 테스트 케이스 수

        for (int tc = 1; tc <= T; tc++) {
            // 붕어빵 먹는 사람 수, 만드는데 걸리는 시간, 시간 당 만들 수 있는 갯수
            int N = sc.nextInt();  // 붕어빵을 먹는 사람 수
            int M = sc.nextInt();  // 만드는 데 걸리는 시간
            int K = sc.nextInt();  // 시간당 만들 수 있는 갯수

            // 각 사람이 언제 도착하는지 시간
            int[] lst = new int[N];
            for (int i = 0; i < N; i++) {
                lst[i] = sc.nextInt();  // 도착 시간 입력
            }

            // 붕어빵 사간 사람 수
            int cnt = 0;
            String ans = "Possible";  // 초기 상태는 가능
            Arrays.sort(lst);  // 도착 시간으로 정렬

            for (int n : lst) {
                cnt++;  // 현재 처리 중인 사람 수 증가
                // 현재 시간이 얼마나 많은 붕어빵을 만들 수 있는지 계산
                if ((n / M) * K < cnt) {
                    ans = "Impossible";  // 붕어빵을 충분히 만들 수 없을 경우
                    break;  // 더 이상 검사할 필요 없음
                }
            }
            System.out.printf("#%d %s\n", tc, ans);  // 결과 출력
        }

        sc.close();  // Scanner 자원 해제
    }
}
