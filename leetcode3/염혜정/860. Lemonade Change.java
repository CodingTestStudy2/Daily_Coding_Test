// O(n)

class Solution {
    public boolean lemonadeChange(int[] bills) {
        int balance_5 = 0;
        int balance_10 = 0;

        for (int bill : bills) {
            int change = bill - 5;
            if (change == 0) {
                balance_5++;
                continue;
            }

            if (change == 5) {
                if (balance_5 < 1) return false;
                balance_5--;
                balance_10++;
            } else if (change == 15) {
                if (balance_5 >= 1 && balance_10 >= 1) {
                    balance_5--;
                    balance_10--;
                } else if (balance_5 >= 3) {
                    balance_5 = balance_5 - 3;
                } else {
                    return false;
                }

            }
        }
        return true;
    }
}
