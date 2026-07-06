/*

1. 아이디어 : 모듈러 연산 활용. k번째 인덱스부터 s 문자열의 길이만큼 붙이기 

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 모듈러 연산

 */

class Solution {
    public String getEncryptedString(String s, int k) {
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<s.length(); i++) {
            int idx = (k+i)%s.length();

            sb.append(s.charAt(idx));
        }

        return sb.toString();
    }
}