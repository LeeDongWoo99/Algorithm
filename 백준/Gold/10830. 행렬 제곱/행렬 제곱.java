import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    final static int MOD = 1000;
    public static int N;
    public static int[][] procession;

    // 행렬 제곱 분할정복 메소드
    public static int[][] pow(int[][] A, long exp) {
        
        if(exp == 1L) {
            return A;
        }
        
        int[][] ret = pow(A, exp / 2);
        
        ret = multiply(ret, ret);
        
        if(exp % 2 == 1L) {
            ret = multiply(ret, procession);
        }

        return ret;
    }

    // o1과 o2 행렬을 곱해주는 메소드
    public static int[][] multiply(int[][] o1, int[][] o2) {

        int[][] ret = new int[N][N];

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                for(int k = 0; k < N; k++) {

                    ret[i][j] += o1[i][k] * o2[k][j];
                    ret[i][j] %= MOD;	
                }
            }
        }
        return ret;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        long B = Long.parseLong(st.nextToken());

        procession = new int[N][N];


        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < N; j++) {
                procession[i][j] = Integer.parseInt(st.nextToken()) % MOD;
            }
        }

        int[][] result = pow(procession, B);

        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                sb.append(result[i][j]).append(' ');
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}