// 1. 아이디어
// 1-1. 평균 구하기
// 1-2. 값이 존재하면 ++

// 2. 시간복잡도
// O(nlogn)

import java.util.*;

class Solution {
    public int smallestAbsent(int[] nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        int avg = sum / nums.length;
        avg += 1;

        Arrays.sort(nums);
        if (avg <= 0) avg = 1;

        for (int num : nums) {
            if (num == avg) avg++;
        }
        return avg;
    }
}
