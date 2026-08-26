// o(n)

class Solution {
    public int[] limitOccurrences(int[] nums, int k) {
        int n = nums.length, idx = 0;
        int[] res = new int[n];
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && nums[j] == nums[i]) j++;
            int count = Math.min(j - i, k);
            for (int c = 0; c < count; c++) res[idx++] = nums[i];
            i = j;
        }
        return java.util.Arrays.copyOf(res, idx);
    }
}
