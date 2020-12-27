import java.util.HashSet;

public class FindDuplicate{
    public static void main(String[] args) {
        int[] a = { 2, 1, 3, 5, 3, 2 };
        int[] b = { 1, 1, 2, 2, 1 };
        int[] c = { 1 };
        int a1 = firstDuplicate1(a);
        int a2 = firstDuplicate2(b);
        int a3 = firstDuplicate2(c);
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);
    }


    /**
     * Given an array a that contains only numbers in the range from 1 to
     * a.length, find the first duplicate number for which the second occurrence
     * has the minimal index. In other words, if there are more than 1
     * duplicated numbers, return the number for which the second occurrence has
     * a smaller index than the second occurrence of the other number does. If
     * there are no such elements, return -1.
     * 
     * Solution 1
     */
    public static int firstDuplicate1(int[] num) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < num.length; i++) {
            int n = num[i];
            if (set.contains(n))
                return n;
            set.add(n);
        }
        return -1;
    }


    /**
     * 
     * Solution 2
     */
    public static int firstDuplicate2(int[] num) {
        for (int i = 0; i < num.length; i++) {
            if (num[Math.abs(num[i]) - 1] < 0)
                return Math.abs(num[i]);
            num[Math.abs(num[i]) - 1] *= -1;
        }
        return -1;
    }
}
