/*

1. 아이디어 : 각 자리수를 순열로 구함. 이때 첫자리는 9이고 그 외 n-1자리는 !(n-1)으로 계산

2. 시간복잡도 : O(8 + N - 2) -> O(N)

3. 자료구조/알고리즘 : 누적합

 */

class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        // 최대 1억
        // 모든 개수, 겹치지 않아야함 

        // n = 1 -> 0 ~ 9 (9)
        // n = 2 -> 10 ~ 99 (9*9)
        // n = 3 -> 100 ~ 999 (9*9*8)
        // n = 4 -> 1000 ~ 9999

        if(n == 0) return 1;

        int ans = 10;

        int[] sum = new int[9];
        sum[0] = 9;
        for(int i=1; i<9; i++) sum[i] = sum[i-1]*(9-i); 

        for(int i=2; i<=n; i++) {
            ans+= 9*sum[i-2];
        }

        return ans;

    }
}