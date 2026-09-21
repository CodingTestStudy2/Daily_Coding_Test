// O(n)

class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length-1; i>=0; i--) {
            int digit = digits[i];
            if (digit == 9) digits[i] = 0;
            else {
                digits[i] = digit + 1;
                break;
            }
        }
        if (digits[0] == 0) {
            int[] temp = new int[digits.length+1];
            temp[0] = 1;
            for (int i = 1; i<temp.length; i++) temp[i] = digits[i-1];
            return temp;
        }
        return digits;
    }
}
