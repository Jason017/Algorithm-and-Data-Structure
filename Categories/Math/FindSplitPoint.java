// https://www.geeksforgeeks.org/split-array-two-equal-sum-subarrays/

public class FindSplitPoint {
    public static void main(String[] args) {

    }

    public static int findSplitPoint(int[] nums) {
        int leftSum = 0, rightSum = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            leftSum += nums[i];
        }

        for (int i = n - 1; i >= 0; i--) {
            rightSum += nums[i];
            leftSum -= nums[i];
            if (rightSum == leftSum)
                return i;
        }

        return -1;
    }
}
