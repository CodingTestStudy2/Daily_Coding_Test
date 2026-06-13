/*

1. 아이디어 : 특별한 문자열을 직접 구해 1의 개수를 계산한다
              1. 숫자는 1부터 시작한다
              2. s = "1221121221221121122……" 로 이미 앞부분은 정해져 있다
              3. 3번째 숫자 2부터 직전숫자가 1이면 2, 2면 1이라는 규칙을 가지고, 문자열을 만든다
              4. n이되면 1의 개수를 return 한다

2. 시간복잡도 : O(N)

3. 자료구조/알고리즘 : 완전탐색, 구현

 */

class Solution {
    public int magicalString(int n) {
        // 최대 10만

        int idx = 3;
        int ans = 1;
        int pointer = 2;

        if(n == 1) return ans;

        StringBuilder sb = new StringBuilder();
        sb.append(122);
        int addNum = 0;

        while(true) {
            int num = sb.charAt(pointer)-'0';
            if(sb.charAt(sb.length()-1) == '2') addNum = 1;
            else addNum = 2;

            while(num>0){
                if(idx >= n) return ans;
                if(addNum == 1) ans++;
                sb.append(addNum);
                idx++;
                num--;
            }

            pointer++;
        }
    }
}