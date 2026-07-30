// x = 0을 제외한 값
// sum = x의 각 값을 더한 값

class Solution {
    public long sumAndMultiply(int n) {
        if (n == 0) return 0;
        
        String s = "";
        long sum = 0;
        while (n>0) {
            int digit = n % 10;
            if (digit != 0) {
                s = digit + s;
                sum += digit;
            }
            n /= 10;
        }
        long x = Long.parseLong(s);
        return x * sum;
    }
}
