/*

1. 아이디어 : 조건에 맞는 최소 인덱스를 구하면 된다
            s[i] == s[n - i - 1]

2. 시간복잡도 : O(N/2)

3. 자료구조/알고리즘 : 조건문

 */

class Solution {
    public int firstMatchingIndex(String s) {
        // s[i] == s[n - i - 1] 인 가장 작은 인덱스 구하기
        // 없으면 -1

        return solve(s);
    }

    private int solve(String s) {
        int n = s.length();

        // n = 5
        // 0 4
        // 1 3
        // 2 2
        for(int i=0; i<(n+1)/2; i++) {
            if(s.charAt(i) == s.charAt(n-i-1)) return i;
        }

        return -1;
    }
}