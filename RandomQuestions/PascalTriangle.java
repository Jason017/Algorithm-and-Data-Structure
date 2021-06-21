import java.util.Scanner;

public class PascalTriangle {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        printPascal(7);
    }

    private static void printPascal(int n) {
        for(int i=0; i<n; i++) {
            String line = "";
            for(int j=0; j<=i; j++) {
                line += binomialCoeff(i,j) + " ";
            }
            System.out.println(line.trim());
        }
    }

    private static int binomialCoeff(int n, int k) {
        int res = 1;
         
        if (k > n - k)
            k = n - k;
             
        for (int i = 0; i < k; ++i){
            res *= (n - i);
            res /= (i + 1);
        }
        return res;
    }
}