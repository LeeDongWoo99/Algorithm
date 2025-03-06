import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String S = br.readLine();  
        char[] data = S.toCharArray();  

        int zeroCount = 0;
        int oneCount = 0;

        if (data[0] == '0') zeroCount++;
        else oneCount++;

        for (int i = 1; i < data.length; i++) {
            if (data[i] != data[i - 1]) {
                if (data[i] == '0') zeroCount++;
                else oneCount++;
            }
        }

        System.out.println(Math.min(zeroCount, oneCount));
    }
}