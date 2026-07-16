/* 

1. 아이디어 : k개만큼 서로 다른 문자열을 남긴채 삭제하는 최소 알파벳 개수를 구한다.

2. 시간복잡도 : O(N)+O(26)+O(26log26)+O(26) => O(N) N: s 문자열의 길이

3. 자료구조/알고리즘 : 문자열 카운팅

 */

class Solution {
    public int minDeletion(String s, int k) {
        int[] word = new int[26];
        int distinct = 0;
        int ans = 0;
        for(int i=0; i<s.length(); i++) word[s.charAt(i)-'a']++;

        for(int i=0; i<26; i++) {
            if(word[i] != 0) distinct++;
        }

        Arrays.sort(word);

        for(int i=0; i<26; i++) {
            if(distinct <= k) break;
            if(word[i]==0) continue;

            ans+=word[i];
            distinct--;
        }

        return ans;
    }
}