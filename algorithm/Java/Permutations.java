import java.util.*;

class Permutations {
    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        dfs(nums, 0, output);
        return output;
    }

    private static void dfs(int[] nums, int level, List<List<Integer>> output) {
        if (level == nums.length) {
            List<Integer> ans = new ArrayList<>();
            for (int i = 0; i < nums.length; i++) {
                ans.add(nums[i]);
            }
            output.add(ans);
        }

        for (int i = level; i < nums.length; i++) {
            swap(nums, i, level);
            dfs(nums, level + 1, output);
            swap(nums, i, level);
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public static void main(String args[]) {
        int[] nums = new int[] { 1, 2, 3 };
        System.out.println(permute(nums));
    }
}