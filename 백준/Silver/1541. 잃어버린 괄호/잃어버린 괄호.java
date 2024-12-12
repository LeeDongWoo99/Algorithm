import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();

        String[] m = n.split("-"); // "-" 기준으로 나누기
        int ans = 0;

        // 첫 번째 부분 처리
        int x = sumOfParts(m[0]);
        ans += x;

        // 나머지 부분 처리
        for (int i = 1; i < m.length; i++) {
            x = sumOfParts(m[i]);
            ans -= x;
        }

        System.out.println(ans);
        sc.close();
    }

    // 문자열을 "+"로 나누고 합산하는 메서드
    private static int sumOfParts(String part) {
        String[] numbers = part.split("\\+"); // "+" 기준으로 나누기
        int sum = 0;
        for (String num : numbers) {
            sum += Integer.parseInt(num); // 각 숫자를 정수로 변환하고 합산
        }
        return sum;
    }
}