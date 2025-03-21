import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int stairsCount = Integer.parseInt(br.readLine());

        int[] stairs = new int[stairsCount + 1];

        for (int i = 1; i <= stairsCount; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[stairsCount + 1];
        if (stairsCount == 1) {
            dp[1] = stairs[1];

        } else if (stairsCount == 2) {
            dp[2] = stairs[2] + stairs[1];

        } else {
            dp[1] = stairs[1];
            dp[2] = stairs[2] + stairs[1];
            dp[3] = Math.max(stairs[1] + stairs[3], stairs[2] + stairs[3]);

            for (int i = 4; i < stairsCount + 1; i++) {
                dp[i] = Math.max(dp[i - 3] + stairs[i] + stairs[i - 1], dp[i - 2] + stairs[i]);
            }
        }
        System.out.println(dp[stairsCount]);
    }
}