class Solution {
    public int longestBalanced(int[] nums) {
        int maxLen = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            Set<Integer> evenSet = new HashSet<>();
            Set<Integer> oddSet = new HashSet<>();

            for (int j = i; j < n; j++) {
                int current = nums[j];

                if (current % 2 == 0) {
                    evenSet.add(current);
                } else {
                    oddSet.add(current);
                }

                if (evenSet.size() == oddSet.size()) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }

        return maxLen;
    }
}