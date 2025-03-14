import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int classTotalCount = Integer.parseInt(br.readLine());

        int[][] classArray = new int[classTotalCount][2];

        for (int i = 0; i < classTotalCount; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            classArray[i][0] = Integer.parseInt(st.nextToken());
            classArray[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(classArray, Comparator.comparingInt(o -> o[0]));

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(classArray[0][1]); 

        for (int i = 1; i < classTotalCount; i++) {
            if (pq.peek() <= classArray[i][0]) {
                pq.poll(); 
            }
            pq.add(classArray[i][1]); 
        }

        System.out.println(pq.size());
    }
}
