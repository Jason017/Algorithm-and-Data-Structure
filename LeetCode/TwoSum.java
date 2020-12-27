package LeetCode;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> num_map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (num_map.containsKey(target - nums[i])) {
                return new int[]{num_map.get(target - nums[i]), i};
            }
            num_map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No match found");
    }
}
