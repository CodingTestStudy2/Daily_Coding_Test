/*

1. 아이디어 : 0을 제외한 숫자를 역순으로 재정렬 후 원래 값과의 차이 계산

2. 시간복잡도 : O(logN)

3. 자료구조/알고리즘 : 단순 계산

 */

class Solution {
    public int mirrorDistance(int n) {
        int original = n;
        int ans = 0;
        int len = String.valueOf(n).length();

        while(n>0) {
            int num = n%10;
            n/=10;
            len--;

            if(num == 0) continue;
            ans+=num*Math.pow(10, len);
        }

        return Math.abs(original-ans);
    }
}