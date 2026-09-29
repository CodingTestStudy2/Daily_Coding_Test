/*

1. 아이디어 : 
    두 문자열 원소의 개수가 같은지 구하기
    카운팅 배열을 사용한다.

2. 시간복잡도 : O(N+26) => O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public boolean isAnagram(String s, String t) {
        int len = s.length();

        if(s.length() != t.length()) return false;

        int[] sCnt = new int[26];
        int[] tCnt = new int[26];

        for(int i=0; i<len; i++) {
            sCnt[s.charAt(i)-'a']++;
            tCnt[t.charAt(i)-'a']++;
        }

        for(int i=0; i<26; i++) {
            if(sCnt[i] != tCnt[i]) return false;
        }

        return true;
    }
}