// o(n log n)
// 최소 필요 에너지 - 실제 소비 에너지가 큰 작업부터 처리

import java.util.Arrays;

class Solution {
    public int minimumEffort(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> {
            int gapA = a[1] - a[0];
            int gapB = b[1] - b[0];
            return Integer.compare(gapB, gapA);
        });

        int minimumEnergy = 0;
        int spentEnergy = 0;

        for (int[] task : tasks) {
            int actual = task[0];
            int minimum = task[1];
            minimumEnergy = Math.max(minimumEnergy, spentEnergy + minimum);
            spentEnergy += actual;
        }

        return minimumEnergy;
    }
}
