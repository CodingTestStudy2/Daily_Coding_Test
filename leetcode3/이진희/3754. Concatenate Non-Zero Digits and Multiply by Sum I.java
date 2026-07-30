/*

1. 아이디어 : 최대 10억이 주어졌을때, 0을 제외한 값에 각 원소의 자릿수 합 곱하기
              while문으로 모든 자릿수 원소를 구한 후 계산해주면 된다.

2. 시간복잡도 : O(9)

3. 자료구조/알고리즘 : 단순 계산

 */

class Solution {
    public long sumAndMultiply(int n) {
        long sum = 0;
        long multi = 0;
        int digit = 0;

        while(n>0) {
            int num = n%10;
            n/=10;
            if(num == 0) continue;

            sum+=num;
            multi += (long)num*Math.pow(10,digit);
            
            digit++;
        }

        return sum*multi;
    }
}