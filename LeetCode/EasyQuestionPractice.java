// 1. Two Sum
class Solution {
    public int[] twoSums(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement))
                return new int[] {i, map.get(complement)};
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No match found.");
    }
}

// 9. Palindrome Number
class Solution {
    public boolean isPalindrome(int x) {
        String str = String.valueOf(x);
        return str.equals(new StringBuilder(str).reverse().toString());
    }
}
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0))
            return false;
        int r = 0;
        while (x > r) {
            r = r * 10 + x % 10;
            x /= 10;
        }
        return x == r || x == r / 10;
    }
}

// 13. Roman to Integer
class Solution {
    public int romanToInt(String s) {
        char lastChar='0';
        int result = 0;
        for(char ch:s.toCharArray()){
            switch(ch){
                case 'I'-> result+=1;
                case 'V'-> result+=lastChar=='I'?3:5;
                case 'X'-> result+=lastChar=='I'?8:10;
                case 'L'-> result+=lastChar=='X'?30:50;
                case 'C'-> result+=lastChar=='X'?80:100;
                case 'D'-> result+=lastChar=='C'?300:500;
                case 'M'-> result+=lastChar=='C'?800:1000;
            }
            lastChar=ch;
        }
        return result;
    }
}

// 26. Remove Duplicates from Sorted Array
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0, j = 1;
        for (; j < nums.length; j++) {
            if(nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}

// 191. Number of 1 Bits
class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int bits = 0;
        int mask = 1;
        for (int i = 0; i < 32; i++){
            if ((n & mask) != 0) bits++;
            mask <<= 1;
        }
        return bits;
    }
}

// 206. Reverse Linked List
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null){
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
}

// 416.
class Solution {
    public int hammingDistance(int x, int y) {
        int count = 0, binary = x ^ y;
        while(binary > 0) {
            count += binary&1;
            binary >>= 1;
        }
        return count;
    }
    
}
class Solution {
    public int hammingDistance(int x, int y) {
        String binary = Integer.toBinaryString(x^y);
        int count = 0;
        for(int i = 0; i < binary.length(); i++)
            if(binary.charAt(i) == '1') 
                count++;
        return count;
    }
}
