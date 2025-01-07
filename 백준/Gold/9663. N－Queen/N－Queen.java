import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int N;
    public static int ans = 0;
    public static int[] v1,v2,v3;

    public static void dfs(int n) {
        if (n == N) {
            ans ++;
            return;
        }

        for (int j = 0; j < N; j++) {
            if (v1[j] == 0 && v2[n - j + (N - 1)] == 0 && v3[n + j] == 0) {
                v1[j] = v2[n - j + (N - 1)] = v3[n + j] = 1;
                dfs(n + 1);
                v1[j] = v2[n - j + (N - 1)] = v3[n + j] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        ans = 0;

        v1 = new int[N];
        v2 = new int[2 * N - 1];
        v3 = new int[2 * N - 1];

        dfs(0);
        System.out.println(ans);
    }
}
