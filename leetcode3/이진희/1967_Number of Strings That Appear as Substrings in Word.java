/*

1. 아이디어 : 각 pattern들이 word의 부분문자열인지 파악

2. 시간복잡도 : O(patterns.length*N*M) (각 비교 문자열의 길이 곱)

3. 자료구조/알고리즘 : 문자열

 */

class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int ans = 0;
        for(String s : patterns) {
            if(word.contains(s)) ans++; 
        }

        return ans;
    }
}