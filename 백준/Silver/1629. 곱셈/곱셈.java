import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {

    public static long C;

    public static long pow(long A, long exponent) {

        // 지수가 1일 경우 A ^ 1 이므로 A를 그대로 반환
        if (exponent == 1) {
            return A % C;
        }

        // 지수의 절반을 해당하는 A ^(exponent / 2) 을 구한다.
        long temp = pow(A, exponent / 2);

        // 지수가 홀수 인 경우
        if (exponent % 2 == 1) {
            return (temp * temp % C) * A % C;
        }
        return temp * temp % C;
    }

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        C = Long.parseLong(st.nextToken());

        System.out.println(pow(A,B));
    }
}