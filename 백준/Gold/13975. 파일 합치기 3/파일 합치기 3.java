import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine()); 

        while (T-- > 0) {
            int K = Integer.parseInt(br.readLine()); 
            PriorityQueue<Long> pq = new PriorityQueue<>(); 
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < K; i++) {
                pq.add(Long.parseLong(st.nextToken())); 
            }

            long totalCost = 0;

            while (pq.size() > 1) {
                long first = pq.poll();  
                long second = pq.poll(); 
                long mergeCost = first + second;
                totalCost += mergeCost;
                pq.add(mergeCost); 
            }

            sb.append(totalCost).append("\n"); 
        }

        System.out.print(sb.toString()); 
    }
}
