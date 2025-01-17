import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int ans = 0;

        while (N >= 0) {
            if (N % 5 == 0) {
                ans += N / 5;
                System.out.println(ans);
                break;
            }
            N -= 3;
            ans += 1;
        }
        if (N < 0) {
            System.out.println(-1);
        }
    }
}