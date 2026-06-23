/* 

1. 아이디어 : 입력된 문자열에서 알파벳을 추출한다. word의 문자열이 알페벳을 전부 포함하는지 확인후 답을 갱신한다.
              이때 알파벳을 전부 포함하는 문자열이 여러개일 경우 가장 짧고, 먼저 오는 문자열을 답으로 한다. 

2. 시간복잡도 : O(문자열 개수)*O(문자열 길이)

3. 자료구조/알고리즘 : 완전탐색, 카운팅 배열

 */

class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        // 모든 문자 포함 
        // 소문자로 정리
        int[] alphabet = new int[26];
        String ans = "";

        for(int i=0; i<licensePlate.length(); i++) {
            char c = licensePlate.charAt(i);
            if(c >= 'a' && c <='z') alphabet[c-'a']++;
            else if(c >= 'A' && c <= 'Z') alphabet[c-'A']++;
        }

        for(String word : words) {
            int[] tmp = new int[26];
            for(int i=0; i<word.length(); i++) {
                char c = word.charAt(i);
                tmp[c-'a']++;
            }

            boolean check = true;
            for(int i=0; i<26; i++) {
                if(tmp[i] < alphabet[i]) {
                    check = false;
                    break;
                }
            }

            if(!check) continue;
            if(ans.equals("")) ans = word;
            else if(ans.length() > word.length()) ans = word;
        }

        return ans;
    }
}