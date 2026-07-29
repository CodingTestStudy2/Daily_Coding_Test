/*

1. 아이디어 : 특수문자와 소문자를 분리하여 reverse
              각각의 문자열을 분리해서 저장후, 문자열의 길이만큼 완전탐색을 돌며 idx를 맨 뒤 부터 탐색
              소문자일 경우 소문자 문자열에서, 특수문자일 경우 특수문자 문자열에서 배치

2. 시간복잡도 : O(N+N)

3. 자료구조/알고리즘 : 완전탐색, 문자열

 */

class Solution {
    public String reverseByType(String s) {
        // 특수문자 reverse
        // 소문자 reverse

        StringBuilder word = new StringBuilder();
        StringBuilder special = new StringBuilder();

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) >= 'a' && s.charAt(i) <= 'z') word.append(s.charAt(i));
            else special.append(s.charAt(i));
        }

        int idxWord = word.length()-1;
        int idxSpecial = special.length()-1;
        StringBuilder ans = new StringBuilder();

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) >= 'a' && s.charAt(i) <= 'z') ans.append(word.charAt(idxWord--));
            else ans.append(special.charAt(idxSpecial--));
        }

        return ans.toString();
    }
}