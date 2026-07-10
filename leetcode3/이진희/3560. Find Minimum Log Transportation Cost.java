/* 

1. 아이디어 : 통나무가 k보다 길면 자른다

2. 시간복잡도 : O(1)

3. 자료구조/알고리즘 : 조건문

 */

class Solution {
    public long minCuttingCost(int n, int m, int k) {
        long ans = 0;
        if(k<n) ans+=(long)(n-k)*k;
        if(k<m) ans+=(long)(m-k)*k; 

        return ans;
    }
}