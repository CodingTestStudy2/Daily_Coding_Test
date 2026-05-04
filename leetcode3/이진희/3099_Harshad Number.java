/*

1. 아이디어 : 각 자리의 숫자의 합을 더하고, 나누어 떨어지는지 확인

2. 시간복잡도 : O(1) -> N은 입력값의 최대 자릿수: 3

3. 자료구조/알고리즘 : 단순계산

 */

class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int original = x;

        while(x>0) {
            sum+=x%10;
            x/=10;
        }

        if(original%sum == 0) return sum;
        return -1;
    }
}