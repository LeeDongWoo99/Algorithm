import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int max_anx = 0;

        for (int i = 0; i < N - 2; i++) {
            for (int j = i + 1; j < N - 1; j++) {
                for (int z = j + 1; z < N ; z++) {
                    int ans = arr[i] + arr[j] + arr[z];
                    if (ans <= M && ans > max_anx) {
                        max_anx = ans;
                    }
                }
            }
        }
        System.out.println(max_anx);
    }
}

