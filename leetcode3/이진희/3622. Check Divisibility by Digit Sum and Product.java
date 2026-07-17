/*

1. 아이디어 : n의 각자릿수의 합과 각 자릿수의 곱을 더하고, n으로 나누어떨어지는지 확인

2. 시간복잡도 : O(logN)

3. 자료구조/알고리즘 : 구현

 */

class Solution {
    public boolean checkDivisibility(int n) {
        int sum = 0;
        int mult = 1;
        int original = n;

        while(n>0) {
            sum+=n%10;
            mult*=n%10;

            n/=10;
        }  

        return original % (sum + mult) == 0;
    }
}