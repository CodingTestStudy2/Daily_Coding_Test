/*

1. 아이디어 : 각 부분 문자열마다 고유 문자 개수를 세고, 매번 3으로 나눈 문자열의 길이와 비교하며, 같은지 확인

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : for문

 */

class Solution {
    public int residuePrefixes(String s) {
        // 각 고유 숫자 개수
        boolean[] word = new boolean[26];
        int cnt = 0;
        int ans = 0;

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if(!word[c-'a']) {
                cnt++;
                word[c-'a'] = true;
            }

            if(cnt == (i+1)%3) ans++;
        }

        return ans;
    }
}