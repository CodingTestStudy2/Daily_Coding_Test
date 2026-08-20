/*

1. 아이디어 : x가 아닌 숫자들을 먼저 붙이고, 이후 x개수만큼 더 붙인다

2. 시간복잡도 : O(N+N)

3. 자료구조/알고리즘 : 완전탐색

 */
class Solution {
    public String rearrangeString(String s, char x, char y) {
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) != x) sb.append(s.charAt(i));
            else cnt++;
        }

        while(cnt-->0) sb.append(x);
        return sb.toString();
    }
}