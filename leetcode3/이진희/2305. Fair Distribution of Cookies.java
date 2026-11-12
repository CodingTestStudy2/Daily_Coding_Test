/* 

1. 아이디어 : 모든 쿠기를 k개로 분배하며 최소 차이가 나는 값 중 가장 큰 값을 구한다
            쿠기가 8개밖에 없으므로 백트랙킹으로 전부 구해본다

2. 시간복잡도 : O(K^n)

3. 자료구조/알고리즘 : 그리디, 커스텀 정렬

 */

class Solution {
    private int ans = 1000000;
    public int distributeCookies(int[] cookies, int k) {
        // 모든 쿠키 분배
        // 차이가 최소가 되어야 한다
        // 쿠키는 최대 8개

        int[] children = new int[k];
        backtrack(cookies, children, 0);

        return ans;
    }

    private void backtrack(int[] cookies, int[] children, int idx) {
        if(idx == cookies.length) {
            int max = 0;
            for(int c : children) max = Math.max(max, c);
            
            ans = Math.min(ans, max);
            return;
        }

        int curMax = 0;
        for(int c : children) curMax = Math.max(curMax, c);

        if(curMax >= ans) return;

        for(int i=0; i<children.length; i++) {
            children[i] += cookies[idx];
            backtrack(cookies, children, idx+1);
            children[i] -= cookies[idx];
        }
    }
}