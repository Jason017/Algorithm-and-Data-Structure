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

        System.out.println(right_bound(nums, target)); // 3
        System.out.println(left_bound(nums, target)); // 1

        System.out.println(binarySearch2_1(nums, target)); // 1
        System.out.println(binarySearch2_2(nums, target)); // 1

        nums = new int[] { 1, 2, 2, 2, 3 };
        target = 2;
        System.out.println(binarySearch1_1(nums, target)); // 2
        System.out.println(binarySearch1_2(nums, target)); // 2

        System.out.println(right_bound(nums, target)); // 3
        System.out.println(left_bound(nums, target)); // 1

        System.out.println(binarySearch2_1(nums, target)); // 1
        System.out.println(binarySearch2_2(nums, target)); // 1
    }

    // Find the position of the target in nums
    public static int binarySearch1_1(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
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
            int m = l + (r - l) / 2;
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

    public static int left_bound(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] < target) {
                // interval: [m+1, r]
                l = m + 1;
            } else if (nums[m] >= target) {
                // interval: [l, m-1]
                // keep moving the right boundary to the left
                r = m - 1;
            }
        }
        // check left boundary
        if (l == nums.length || nums[l] != target)
            return -1;
        return l;
    }

    public static int right_bound(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] <= target) {
                // interval: [m+1, r]
                // keep moving the left bound to the right
                l = m + 1;
            } else if (nums[m] > target) {
                // interval: [l, m-1]
                r = m - 1;
            }
        }
        // check right boundary
        if (r == -1 || nums[r] != target)
            return -1;
        return r;
    }

    // Find the position to insert target in nums
    // Find the number of elements smaller than target in nums
    public static int binarySearch2_1(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] >= target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    // Find the position to insert target in nums
    // Find the number of elements smaller than target in nums
    public static int binarySearch2_2(int[] nums, int target) {
        int l = 0, r = nums.length;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] >= target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
}