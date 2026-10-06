/*

1. 아이디어 : 문자열에서 숫자와 알파벳만 별도로 변환 후 펠린드롬 여부 체크

2. 시간복잡도 : O(2N) => O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public boolean isPalindrome(String s) {
        // 소문자, 숫자만
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);

            if(c>='a' && c<='z') sb.append(c);
            else if(c>='A' && c<='Z') sb.append((char)(c+32));
            else if(c>='0' && c<='9') sb.append(c);
        }

        return isPalindrome(sb);
    }

    private boolean isPalindrome(StringBuilder sb) {
        int l = 0;
        int r = sb.length()-1;

        while(l<r) {
            if(sb.charAt(l++) != sb.charAt(r--)) return false;
        }
        return true;
    }
}