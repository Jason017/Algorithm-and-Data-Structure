// https://www.geeksforgeeks.org/longest-common-subarray-in-the-given-two-arrays/
public class LongestCommonSubarray {
    public static void main(String[] args) {
        int[] a = { 1, 2, 8, 2, 1 };
        int[] b = { 8, 2, 1, 4, 7 };

        System.out.println(longestCommonSubarray(a, b)); // 3
    }

    public static int longestCommonSubarray(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;
        int[][] memo = new int[n1 + 1][n2 + 1];
        int ans = 0;
        for (int i = n1 - 1; i >= 0; i--) {
            for (int j = n2 - 1; j >= 0; j--) {
                if (nums1[i] == nums2[j]) {
                    memo[i][j] = memo[i + 1][j + 1] + 1;
                    ans = Math.max(ans, memo[i][j]);
                }
            }
        }
        return ans;
    }

    public static int longestCommonSubarray1(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;
        int[][] memo = new int[n1 + 1][n2 + 1];
        int ans = 0;
        for (int i = 1; i <= n1; i++) {
            for (int j = 1; j <= n2; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    memo[i][j] = memo[i - 1][j - 1] + 1;
                    ans = Math.max(ans, memo[i][j]);
                }
            }
        }
        return ans;
    }
}
