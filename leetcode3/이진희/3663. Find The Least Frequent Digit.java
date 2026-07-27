/*

1. 아이디어 : 숫자의 빈도수 계산 후, 가장 빈도수가 적은 숫자 반환
              정답이 여러개일 경우 더 작은 숫자 반환
              각 숫자를 카운팅하여 계산 후 해결

2. 시간복잡도 : O(31 + 10) => O(1)

3. 자료구조/알고리즘 : 배열

 */

class Solution {
    public int getLeastFrequentDigit(int n) {
        int[] nums = new int[10];

        while(n > 0) {
            int num = n%10;
            nums[num]++;

            n/=10;
        }   

        int minNum = 0;
        int minCnt = 100;
        for(int i=0; i<10; i++) {
            if(nums[i] == 0 || minCnt<=nums[i]) continue;

            minNum = i;
            minCnt = nums[i];
        }

        return minNum;
    }
}