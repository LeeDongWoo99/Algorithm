import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int result = 0;

        for (int M = 1; M <= N; M++) {
            int sumNum = M + digitSum(M); 

            if (sumNum == N) { 
                result = M;
                System.out.println(result);
                break;
            }
            if (M == N) {
                System.out.println(0);
            }
        }
    }

    // 각 자릿수의 합을 구하는 메서드
    public static int digitSum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10; 
            num /= 10;       
        }
        return sum;
    }
}