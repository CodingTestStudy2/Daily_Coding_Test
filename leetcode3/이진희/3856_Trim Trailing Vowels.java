/*

1. 아이디어 : 문자열 뒤부터 검사하여 자음이면 위치를 저장하고 break
            이때 전부 모음으로 이루어진 문자열일 수 있으므로, -1로 초기화 해준다.

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public String trimTrailingVowels(String s) {
        int idx = -1;

        // 맨끝 모음 지우기
        for(int i=s.length()-1; i>=0; i--) {
            char c = s.charAt(i);
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') continue;
            else {
                idx = i;
                break;
            }
        }

        if(idx == -1) return "";
        else return s.substring(0,idx+1);
    }
}