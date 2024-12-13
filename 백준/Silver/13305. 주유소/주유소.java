import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        int[] dis = new int[N - 1];
        for (int i = 0; i < N - 1; i++) {
            dis[i] = sc.nextInt();
        }
        
        int[] oil = new int[N];
        for (int i = 0; i < N; i++) {
            oil[i] = sc.nextInt();
        }
        
        int minOil = oil[0]; 
        long ans = (long) dis[0] * minOil; 
        
        for (int cur = 1; cur < N - 1; cur++) {
            if (minOil > oil[cur]) {
                minOil = oil[cur]; 
            }
            ans += (long) minOil * dis[cur]; 
        }
        
        System.out.println(ans);

        sc.close();
    }
}