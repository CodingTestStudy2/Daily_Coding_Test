/*

1. 아이디어 : 문자열이 주어졌을때 같은 문자열이 붙어있으면 안됨. 
              조건
              0과 1의 개수 차이가 1이상이면 '11' '00'과 같은 패턴이 생겨 만들 수 없다. 
              완전 탐색을 돌려 각 1과 0의 개수차이가 1 이하인지 확인한다.

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색

 */

class Solution {
    public int countValidPrefixes(String s) {
        // 00101
        // 0과 1 번갈아 배치 
        int zero = 0;
        int one = 0;
        int ans = 0;

        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i) == '0') zero++;
            else one++;

            if(Math.abs(zero-one) <= 1) ans++;
        }

        return ans;
    }
}