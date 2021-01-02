package Example;

import java.util.Arrays;

public class Permutation {
    public static void main(String[] args) {
        String str = "ABC";
        //permutation("", str);
        long startTime = System.currentTimeMillis();
        permute("", str);
//        permutation1(str, 0, str.length() - 1);
//        permutation2(str.toCharArray(), 0);
//        permutation3(str);
        long endTime = System.currentTimeMillis();
        System.out.println("Took " + (endTime - startTime) + " ms");


    }


    //    private static void permutation(String candidate, String remaining) {
    //        if (remaining.length() == 0)
    //            System.out.println(candidate);
    //        for (int i = 0; i < remaining.length(); i++) {
    //            String newCandidate = candidate + remaining.charAt(i);
    //            String newRemaining = remaining.substring(0, i) + remaining.substring(i + 1);
    //            permutation(newCandidate, newRemaining);
    //        }
    //    }

    // Find all permutations of a given String using recursion
    // Took 17 ms
    private static void permute(String perm, String word) {
        if (word.isEmpty()) {
            System.out.println(perm + word);
        } else {
            for (int i = 0; i < word.length(); i++)
                permute(perm + word.charAt(i), word.substring(0, i) + word.substring(i + 1));
        }
    }

    // Took 0 ms
    private static void permutation1(String str, int l, int r) {
        if (l == r)
            System.out.println(str);
        for (int i = l; i <= r; i++) {
            str = swap1(str, l, i);
            permutation1(str, l + 1, r);
            str = swap1(str, l, i);
        }
    }


    public static String swap1(String str, int i, int j) {
        char temp;
        char[] charArray = str.toCharArray();
        temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }
    
    // Took 0 ms
    private static void permutation2(char[] chars, int currentIndex) {
        if (currentIndex == chars.length - 1)
            System.out.println(String.valueOf(chars));
        for (int i = currentIndex; i < chars.length; i++) {
            swap2(chars, currentIndex, i);
            permutation2(chars, currentIndex + 1);
            swap2(chars, currentIndex, i);
        }
    }


    private static void swap2(char[] chars, int i, int j) {
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
    }

    // Find all permutations of a given String using iteration
    // Took 9 ms
    private static void permutation3(String str) {
        int n = str.length();
        char[] s = str.toCharArray();
        Arrays.sort(s);

        while (true) {
            System.out.println(String.valueOf(s) + " ");

            int i = n - 1;
            while (s[i - 1] >= s[i]) {
                if (--i == 0)
                    return;
            }
            int j = n - 1;
            while (j > i && s[j] <= s[i - 1])
                j--;
            swap2(s, i - 1, j);
            reverse(s, i, n - 1);
        }

    }

    private static void reverse(char[] chars, int i, int j) {
        while (i < j)
            swap2(chars, i++, j--);
    }
}
