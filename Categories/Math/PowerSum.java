import java.util.ArrayList;

// https://www.geeksforgeeks.org/powers-2-required-sum/
import java.util.*;

public class PowerSum {
    public static void main(String[] args) {
        List<Integer> ans = PowerSum.solution(71307);
        System.out.println(ans);
    }

    public static List<Integer> solution(int num) {
        List<Integer> bins = new ArrayList<>();
        List<Integer> indeces = new ArrayList<>();

        while (num > 0) {
            bins.add(num % 2);
            num /= 2;
        }

        for (int i = 0; i < bins.size(); i++) {
            if (bins.get(i) == 1) {
                indeces.add(i);
            }
        }
        // return bins;
        return indeces;
    }
}
