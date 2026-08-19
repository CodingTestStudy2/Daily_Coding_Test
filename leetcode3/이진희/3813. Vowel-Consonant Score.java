/*

1. 아이디어 : 문자열 자음 모음 개수 세서 나눠주기, 이때 자음이 0이면 계산이 안되므로 0 반환

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 계산

 */

class Solution {
    public int vowelConsonantScore(String s) {
        int v = 0;
        int k = 0;

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') v++;
            else if(c>='a' && c<='z') k++;
        }

        if(k == 0) return 0;
        return (int)Math.floor(v/k);
    }
}