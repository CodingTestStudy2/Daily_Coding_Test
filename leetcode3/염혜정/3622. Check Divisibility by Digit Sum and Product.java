// n을 각 자릿수를 더한 sum / 곱한 값인 product를 더한 값으로 나눠준다.
// O(log n)

class Solution {
    public boolean checkDivisibility(int n) {
        int sum = 0;
        int product = 1;
        int temp = n;

        while (temp>0) {
            int digit = temp % 10;
            sum += digit;
            product *= digit;
            temp /= 10;
        }

        boolean result = n % (sum+product) == 0? true: false;
        return result;
    }
}
