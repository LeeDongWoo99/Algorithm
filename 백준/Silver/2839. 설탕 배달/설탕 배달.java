import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sugar = sc.nextInt(); // 설탕 무게 입력
        int bag = 0; // 봉지 수 초기화

        // 설탕 무게가 0 이상일 때 반복
        while (sugar >= 0) {
            if (sugar % 5 == 0) { 
                bag += (sugar / 5); 
                System.out.println(bag); 
                break; 
            }
            sugar -= 3; 
            bag += 1; 
        }
        
        // 3과 5로 나눠지지 않으면 -1 출력
        if (sugar < 0) {
            System.out.println(-1);
        }
    }
}