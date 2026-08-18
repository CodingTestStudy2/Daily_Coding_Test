/* 

1. 아이디어 : 문자열의 배열마다 각 배열 가중치를 센 후 모듈러 연산으로 나눠서 나온값을 알파벳 변환한다

              이때, z=0, a=25 처럼 반대로 계산해야 한다.

2. 시간복잡도 : O(100*10)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder sb = new StringBuilder();
        for(String s : words) {
            int cnt = 0;
            for(int i=0; i<s.length(); i++) {
                cnt+=weights[s.charAt(i)-'a'];
            }

            char c = (char)('z'-cnt%26);
            sb.append(c);
        }

        return sb.toString();
    }
}