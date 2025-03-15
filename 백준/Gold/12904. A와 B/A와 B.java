import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder inputS = new StringBuilder(br.readLine());
        StringBuilder inputT = new StringBuilder(br.readLine());

        while (inputS.length() < inputT.length()) {
            if (inputT.charAt(inputT.length() -1 ) == 'A') {
                inputT.deleteCharAt(inputT.length() -1);

            } else if (inputT.charAt(inputT.length() -1 ) == 'B') {
                inputT.deleteCharAt(inputT.length() -1);
                inputT.reverse();
            }
        }
        if (inputT.toString().equals(inputS.toString())) {
            System.out.println(1);

        } else {
            System.out.println(0);
        }
    }
}