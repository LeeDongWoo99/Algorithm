import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int st = 666;
        int count = 0;
        ArrayList<Integer> lst = new ArrayList<>();

        while (true) {
            if (String.valueOf(st).contains("666")) { // 문자열로 변환 후 "666" 포함 여부 확인
                lst.add(st);
                count++;
                if (count == N) {
                    break;
                }
            }
            st++;
        }

        System.out.println(lst.get(N - 1)); 
    }
}