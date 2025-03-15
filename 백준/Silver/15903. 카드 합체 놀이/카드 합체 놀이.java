import java.io.*;
import java.util.*;


public class Main {

    static PriorityQueue<Long> pq = new PriorityQueue<>();
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int cardCount = Integer.parseInt(st.nextToken());
        int sumCount = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        long cardSum = 0;

        for (int i = 0; i < cardCount; i++) {
            pq.add(Long.parseLong(st.nextToken()));
        }

        for (int i = 0; i < sumCount; i++) {
            Long minNum1 = pq.poll();
            Long minNum2 = pq.poll();
            pq.add(minNum1 + minNum2);
            pq.add(minNum1 + minNum2);
        }

        while (!pq.isEmpty()) {
            cardSum += pq.poll();
        }
        System.out.println(cardSum);
    }
}