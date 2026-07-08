import java.util.*;

class Solution {
    public int minimumPairRemoval(int[] nums) {
        int operations = 0;
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }

        while (!isSorted(list)) {
            int minSum = Integer.MAX_VALUE;
            int target = -1;

            for (int i = 0; i < list.size() - 1; i++) {
                int sum = list.get(i) + list.get(i + 1);
                if (sum < minSum) {
                    minSum = sum;
                    target = i;
                }
            }

            list.set(target, minSum);
            list.remove(target + 1);
            
            operations++;
        }

        return operations;
    }

    private boolean isSorted(List<Integer> list) {
        for (int i = 0; i < list.size() - 1; i++) {
            if (list.get(i) > list.get(i + 1)) {
                return false;
            }
        }
        return true;
    }
}