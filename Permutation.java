package Example;

public class Permutation {
    public static void main(String[] args) {
        String str = "ABC";
        permutation("", str);
        System.out.println();
        permutation1(str, 0, str.length() - 1);
        System.out.println();
        permutation2(str.toCharArray(), 0);

    }


    private static void permutation(String candidate, String remaining) {
        if (remaining.length() == 0)
            System.out.println(candidate);
        for (int i = 0; i < remaining.length(); i++) {
            String newCandidate = candidate + remaining.charAt(i);
            String newRemaining = remaining.substring(0, i) + remaining.substring(i + 1);
            permutation(newCandidate, newRemaining);
        }
    }


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
}
