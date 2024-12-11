import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();   // 돈을 인출한 사람 수
        int tot = 0;    // 현재 사람이 돈을 인출하는데 걸리는 시간
        int ans = 0;    // 모든 인원이 돈을 인출하는데 걸리는 시간
        int[] P = new int[N];   // 각 사람이 돈을 인출하는데 걸리는 시간
        
        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }
        
        Arrays.sort(P);     // 오름차순으로 정렬
        
        for (int i = 0; i < N; i++) {
            tot += P[i];
            ans += tot;
        }
        System.out.println(ans);
    }
}