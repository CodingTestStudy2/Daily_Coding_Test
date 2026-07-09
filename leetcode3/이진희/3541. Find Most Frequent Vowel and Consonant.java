/* 

1. 아이디어 : 한 모음의 최대 빈도수, 한 자음의 최대 빈도수 합을 구한다.
              각 알파벳 빈도수를 카운팅 후, 모음만 따로 처리한다.

2. 시간복잡도 : O(N) + O(26) = O(N) (N: s의 길이)

3. 자료구조/알고리즘 :

 */

class Solution {
    public int maxFreqSum(String s) {
        // 최대 자음 빈도수
        // 최대 모음 빈도수

        int[] word = new int[26];
        for(int i=0; i<s.length(); i++) {
            word[s.charAt(i)-'a']++;
        }

        int vCnt = 0;
        int cCnt = 0;

        // 0, 4, 8, 14, 20 
        for(int i=0; i<26; i++) {
            if(i == 0 || i == 4 || i == 8 || i == 14 || i == 20) {
                vCnt = Math.max(vCnt, word[i]);
            }
            else cCnt = Math.max(cCnt, word[i]);
        }

        return vCnt + cCnt;
    }
}