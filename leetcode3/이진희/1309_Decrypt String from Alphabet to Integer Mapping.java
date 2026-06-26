/* 

1. 아이디어 : 문자열 뒤부터 계산
              현재 문자가 '#'이면 바로 앞의 두 자리 숫자를 하나의 문자로 기록
              '#'이 아니면 한 자리 숫자를 문자로 변환
              뒤부터 기록했기 때문에 reverse해서 반환

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public String freqAlphabets(String s) {
        StringBuilder sb = new StringBuilder();
        int i = s.length() - 1;

        while (i >= 0) {
            if (s.charAt(i) == '#') {
                String numStr = s.substring(i - 2, i);
                int num = Integer.parseInt(numStr);
                
                sb.append((char) ('a' + num - 1));
                
                i -= 3;
            } else {
                int num = s.charAt(i) - '0';
                sb.append((char) ('a' + num - 1));    
                i -= 1;
            }
        }

        return sb.reverse().toString();
    }
}