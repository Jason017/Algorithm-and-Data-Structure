import java.util.*;

public class ArrayQueue {
    private static int[] nums;
    private static int target;

    public static void main(String[] main) {
        nums = new int[] { -1, 0, 3, 5, 9, 12 };
        target = 9;
        System.out.println(binarySearch2(nums, target)); // 4
        target = 2;
        System.out.println(binarySearch1(nums, target)); // -1
        System.out.println(binarySearch3(nums, target)); // 2
    }

    // Find the position of the target in nums
    public static int binarySearch1(int[] nums, int target) {
        int l = 0, h = nums.length - 1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                h = m - 1;
            }
        }
        return -1;
    }

    // Find the position to insert target in nums
    public static int binarySearch2(int[] nums, int target) {
        int l = 0, h = nums.length - 1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (nums[m] >= target) {
                h = m - 1;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    // Find the position to insert target in nums
    public static int binarySearch3(int[] nums, int target) {
        int l = 0, h = nums.length;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (nums[m] >= target) {
                h = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
}