/*

1. 아이디어 : 최대 10억의 숫자를 각 자릿수 순서대로 배열 저장, 각 원소를 분리한뒤, 자릿수(2,3,4..)에 맞게 곱한 뒤 배열로 저장하면 된다.

2. 시간복잡도 : O(9+9) => O(1) (최대 수의 길이)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public int[] decimalRepresentation(int n) {
        StringBuilder sb = new StringBuilder();

        while(n>0) {
            sb.append(n%10);
            n/=10;
        }

        int[] ans = new int[sb.length()];
        int multi = (int)Math.pow(10,sb.length()-1);
        int idx = 0;
        int cnt = sb.length();

        for(int i=ans.length-1; i>=0; i--) {
            if(sb.charAt(i)-'0' == 0) cnt--;
            else ans[idx++] = (sb.charAt(i)-'0')*multi;
            multi/=10;
        }

        return Arrays.copyOf(ans, cnt);
    }
}