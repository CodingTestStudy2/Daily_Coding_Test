// o(logn)

class Solution {
    public int mirrorDistance(int n) {
        int temp = n;
        int reverse = 0;
        while (temp>0) {
            int digit = temp%10;
            reverse = 10*reverse + digit;
            temp /= 10;
        }
        return Math.abs(n - reverse);
    }
}
