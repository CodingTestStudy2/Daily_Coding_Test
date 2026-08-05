
/*

1. 아이디어 : 정확히 "11"이 한 쌍 존재하는지 파악
              숫자를 이진수 변환하며 "11"이 한쌍만 존재하는지 체크

2. 시간복잡도 : O(logN)

3. 자료구조/알고리즘 : 조건문

 */

class Solution {
    public boolean consecutiveSetBits(int n) {

        StringBuilder sb = new StringBuilder();
        boolean check = false;

        while(n>1) {
            int num = n%2;
            sb.insert(0,num);

            if(sb.length()>1 && num == 1 && sb.charAt(0) == sb.charAt(1)) {
                if(check) return false;
                check = true;
            }
            n/=2;
        }

        sb.insert(0,n);
        
        if(n == 1) {
            if(sb.length()>1 && n == 1 && sb.charAt(0) == sb.charAt(1)) {
                if(check) return false;
                check = true;
            }
        }
        
        return check;
    }
}