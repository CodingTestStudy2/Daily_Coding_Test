/*

1. 아이디어 : x를 a+b로 나누었을때 최소 비용
             1 + x-1로 1이 될때까지 나누면 최소

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 그리디

 */

class Solution {
    public int minCost(int n) {
        int ans = 0;

        for(int i=1; i<n; i++) {
            ans += 1*i;
        }

        return ans;
    }
}