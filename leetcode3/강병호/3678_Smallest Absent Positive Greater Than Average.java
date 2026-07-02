class Solution {
    public int smallestAbsent(int[] nums) {
        int sum = 0;
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            sum += num;
            set.add(num);
        }

        double average = (double) sum / nums.length;

        int candidate = (int) Math.floor(average) + 1;
        if (candidate <= 0) candidate = 1; // must be positive

        while (set.contains(candidate)) {
            candidate++;
        }

        return candidate;
    }
}