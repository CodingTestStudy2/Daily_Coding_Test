// 0 ~ 9
// O(log n)

class Solution {
    public int digitFrequencyScore(int n) {
        int result = 0;
        while (n>0) {
            int digit = n % 10;
            result += digit;
            n /= 10;
        }
        return result;
    }
}
