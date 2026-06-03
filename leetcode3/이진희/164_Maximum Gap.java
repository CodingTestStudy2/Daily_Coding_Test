/* 2차 풀이

1. 아이디어 : 기수정렬(Radiz Sort)활용
            최대 자릿수 고정, 음수 없음
            각 자릿수마다 Counting Sort를 하여 계산

2. 시간복잡도 : 1. 정렬 -> O(최대 자릿수*N) -> O(10*N) -> O(N)
             2. 완전탐색 -> O(N)
             
             O(N) + N(N) => O(N)

   공간복잡도 : 1. sortedArray: O(N)
             2. cnt배열: O(10) -> O(1)

             O(N)

3. 자료구조/알고리즘 : 기수정렬 + 완전탐색

 */

// 기수 정렬(Radix Sort)
class Solution {
    public int maximumGap(int[] nums) {
        // 최대 자릿수 10자리 고정
        // 음수 고려 X

        if(nums.length < 2) return 0;

        radixSort(nums);

        int maxGap = 0;
        for(int i=1; i<nums.length; i++) {
            maxGap = Math.max(maxGap, nums[i] - nums[i-1]);
        }

        return maxGap;
    }

    private void radixSort(int[] nums) {
        if (nums.length <=1) return;

        int maxNum = nums[0];
        for(int i : nums) {
            maxNum = Math.max(maxNum, i);
        }

        for(int exp = 1; maxNum/exp>0; exp*=10) {
            countingSort(nums, exp);
        }

    }

    private void countingSort(int[] nums, int exp) {
        int len = nums.length;

        int[] sortedArray = new int[len];
        int[] cnt = new int[10];

        for(int num : nums) {
            int digit = (num/exp)%10;
            cnt[digit]++;
        }

        // 뒤부터 계산하여 위치 판단
        for(int i=1; i<10; i++) cnt[i] += cnt[i-1];

        // 중복 고려
        for(int i = len-1; i>=0; i--) {
            int digit = (nums[i]/exp)%10;
            sortedArray[cnt[digit]-1] = nums[i];
            cnt[digit]--;
        }

        // 각 정렬된 자릿수를 nums 배열에 복사
        System.arraycopy(sortedArray, 0, nums, 0, len);
    }
}

/* 1차 풀이 -> 문제 파악 실패 (시간, 공간 복잡도가 O(N)이어야만 함)

1. 아이디어 : 정렬 상태에서 인접한 원소의 최대 차이를 구하면 된다

2. 시간복잡도 : O(NlogN) + O(N) => O(NlogN)

3. 자료구조/알고리즘 : 정렬 + 완전탐색

 */

class Solution {
    public int maximumGap(int[] nums) {
        //최대 10만
        return solve(nums);
    }

    private int solve(int[] nums) {
        if(nums.length<2) return 0;
        Arrays.sort(nums);
        int maxDiff = -1;

        for(int i=0; i<nums.length-1; i++) {
            maxDiff = Math.max(maxDiff, nums[i+1]-nums[i]);
        }

        return maxDiff;
    }
}