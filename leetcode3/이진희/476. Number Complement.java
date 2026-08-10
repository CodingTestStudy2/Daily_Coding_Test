/*

1. 아이디어 : 10진법을 이진법으로 바꾸고, 1과 0을 바꾼 후, 값을 계산하는 문제
              10진법이 포함되는 이진법의 범위를 파악후, 원래 값의 num을 빼면 된다

2. 시간복잡도 : O(31)

3. 자료구조/알고리즘 : 비트 연산

 */

class Solution {
    public int findComplement(int num) {
        int sum = 1;
        int idx = 1;
        while(num>sum) {
            sum += idx*2;
            idx*=2;
        }

        return sum - num;
    }
}