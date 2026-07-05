/*
* 1. 시간 복잡도 : O(N^2)
* 2. start 인덱스 기준 k번째 문자를 result에 추가, 최대 길이 넘어가는 경우 index 수정 (i + k) % s.length();
*/

class Solution {
    public String getEncryptedString(String s, int k) {
        // start 기준 다음 k 번째 문자
        String result = "";

        for (int i = 0; i < s.length(); i++) {
            int final_index = (i + k >= s.length()) ? (i + k) % s.length() : i + k;
            result = result + s.charAt(final_index);
        }

        return result;
    }
}