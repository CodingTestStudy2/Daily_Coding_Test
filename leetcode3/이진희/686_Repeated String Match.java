/*

1. 아이디어 : a문자열을 여러번 덧붙여서 b가 포함될 수 있는지 확인한다.
              1. a를 b의 길이 이상이 될때까지 붙여보며 포함하는지 확인
              2. b이상의 길이여도 포함하지 않을 경우 한번더 a문자열을 붙여 체크
              3. 그래도 포함하지 않으면 -1 반환

2. 시간복잡도 : O(b/a)+1 + O(N*M) (N = 원본 문자열 길이, M = 찾으려는 문자열 길이) 

3. 자료구조/알고리즘 : 문자열

 */

class Solution {
    public int repeatedStringMatch(String a, String b) {
        // 최대 10,000자
        // b가 a의 substring인가

        int aLen = a.length();
        int bLen = b.length();

        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        while(true) {
            if(sb.length()>=bLen) break;
            cnt++;
            sb.append(a);
            if(sb.indexOf(b) != -1) return cnt; 
        }

        sb.append(a);
        if(sb.indexOf(b) != -1) return cnt+1;
        return -1;
    }
}