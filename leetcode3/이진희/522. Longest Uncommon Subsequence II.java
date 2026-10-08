/*

1. 아이디어 : 모든 주어진 문자열중 중복된 부분문자열이 아닌 문자열중 가장 긴 문자열의 길이와 개수를 구한다.

2. 시간복잡도 : O(N^2*N)

3. 자료구조/알고리즘 : 투포인터, 완전탐색

 */

class Solution {
    public int findLUSlength(String[] strs) {
        // 안겹치는 가장 긴 문자열의 길이 (모든 문자열 중)

        int ans = -1;

        // aba cdc eae
        // aa aaa aaa

        for(int i=0; i<strs.length; i++) {
            boolean check = true;
            for(int j=0; j<strs.length; j++) {
                if(i == j) continue;
                if(strs[i].length() > strs[j].length()) continue;

                if(isSubsequence(strs[i], strs[j])) check = false;
            } 

            if(check) ans = Math.max(ans, strs[i].length());
        }

        return ans;
    }

    private boolean isSubsequence(String s1, String s2) {
        int idx1 = 0;
        int idx2 = 0;

        while(idx1<s1.length() && idx2<s2.length()) {
            if(s1.charAt(idx1) == s2.charAt(idx2)) idx1++;
            idx2++;
        }

        return idx1 == s1.length();
    }
}