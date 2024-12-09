import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        Integer [] lst = new Integer[N];
        int ans = 0;

        // 배열에 동전 종류 넣기
        for (int i = 0; i < N; i++) {
            lst[i] = sc.nextInt();
        }
        // 배열 내림차순으로 정렬
        Arrays.sort(lst, Collections.reverseOrder());

        for (int i = 0; i< N; i++) {
            if (lst[i] > K) {
                continue;
            }
            ans += K / lst[i];
            K = K % lst[i];
            if (K == 0) {
                break;
            }
        }
        System.out.println(ans);
    }
}