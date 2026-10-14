class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] count = new int[101];
        int maxCount = 0;

        for (int num : nums) {
            count[num]++;
            maxCount = Math.max(maxCount, count[num]);
        }

        int[] answer = new int[nums.length];
        int index = 0;

        for (int round = 1; round <= maxCount; round++) {
            for (int value = 1; value <= 100; value++) {
                if (count[value] >= round) {
                    answer[index++] = value;
                }
            }
        }

        return answer;
    }
}
