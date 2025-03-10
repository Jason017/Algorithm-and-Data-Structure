import java.util.*;

public class BinarySearch {
    private static int[] nums;
    private static int target;

    public static void main(String[] main) {
        // nums = new int[] { -1, 0, 3, 5, 9, 12 };
        // target = 9;
        // System.out.println(binarySearch1_1(nums, target)); // 4
        // System.out.println(binarySearch1_2(nums, target)); // 4
        // System.out.println(binarySearch2_1(nums, target)); // 4
        // System.out.println(binarySearch2_2(nums, target)); // 4

        // nums = new int[] { -1, 0, 3, 5, 9, 12 };
        // target = 2;
        // System.out.println(binarySearch1_1(nums, target)); // -1
        // System.out.println(binarySearch1_2(nums, target)); // -1
        // System.out.println(binarySearch2_1(nums, target)); // 2
        // System.out.println(binarySearch2_2(nums, target)); // 2

        nums = new int[] { 1, 4, 5, 7, 9 };
        target = 3;
        System.out.println(binarySearch1_1(nums, target)); // -1
        System.out.println(binarySearch1_2(nums, target)); // -1

        System.out.println(rightBound(nums, target)); // 0
        System.out.println(leftBound(nums, target)); // 1

        nums = new int[] { 1, 2, 2, 2, 3 };
        target = 2;
        System.out.println(binarySearch1_1(nums, target)); // 2
        System.out.println(binarySearch1_2(nums, target)); // 2

        System.out.println(rightBound(nums, target)); // 3
        System.out.println(leftBound(nums, target)); // 1
    }

    // Find the position of the target in nums
    public static int binarySearch1_1(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        // iterate until right boundary is greater than left boundary
        while (l <= r) {
            int m = l + (r - l) / 2; // avoid integer overflow in java
            // System.out.println("l:" + l + " r:" + r + " m:" + m);
            if (nums[m] == target) {
                return m;
            } else if (nums[m] > target) {
                // interval: [l, m-1]
                r = m - 1;
            } else {
                // interval: [m+1, r]
                l = m + 1;
            }
        }
        return -1;
    }

    // Find the position of the target in nums
    public static int binarySearch1_2(int[] nums, int target) {
        int l = 0, r = nums.length;
        while (l < r) {
            int m = l + (r - l) / 2; // avoid integer overflow in java
            // System.out.println("l:" + l + " r:" + r + " m:" + m);
            if (nums[m] == target) {
                return m;
            } else if (nums[m] > target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return -1;
    }

    // Find the leftmost index of element bigger than or equal to target
    // Find the number of element bigger than target
    // Find the leftmost index of consecutive element
    // Find the position to insert target
    public static int leftBound(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2; // avoid integer overflow in java
            if (nums[m] >= target) {
                // keep moving the right boundary to the left
                // interval: [l, m-1]
                r = m - 1;
            } else {
                // if (nums[m] < target)
                // interval: [m+1, r]
                l = m + 1;
            }
        }
        // check left boundary
        // if (l == nums.length || nums[l] != target)
        // return -1;
        return l;
    }

    // Find the rightmost index of element smaller than or equal to target
    // Find the number of element smaller than target
    // Find the rightmost index of consecutive element
    public static int rightBound(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2; // avoid integer overflow in java
            if (nums[m] <= target) {
                // keep moving the left bound to the right
                // interval: [m+1, r]
                l = m + 1;
            } else {
                // if (nums[m] > target)
                // interval: [l, m-1]
                r = m - 1;
            }
        }
        // check right boundary
        // if (r == -1 || nums[r] != target)
        // return -1;
        return r;
    }
}